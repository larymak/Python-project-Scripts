"""
	You need to install the ttkbootstrap, pip install ttkbootstrap(I recomand to use a virtual environment)
"""
import ttkbootstrap as ttk

from widgets import Button, OutputLabel, NumberButtons
from configuration import (
	APP_SIZE, FONT, NORMAL_FONT_SIZE, OUTPUT_FONT_SIZE,
	MAIN_ROW, MAIN_COLUMN,
	NUMBER_POSITIONS, MATH_POSITIONS, MATH_OPERATORS
	)

try:
	from ctypes import windll, byref, sizeof, c_int
except Exception:
	pass


class CalculatorApp(ttk.Window):
	def __init__(self):
		super().__init__(themename = 'superhero')
		self.resizable(False, False)
		self.bind('<Alt-s>', lambda e: self.destroy())
		# setup
		self.title("")
		self.left: int = int((self.winfo_screenwidth() - APP_SIZE[0]) / 2)
		self.top: int = int((self.winfo_screenheight() - APP_SIZE[1]) / 2)
		self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}+{self.left}+{self.top}")
		try:
			self.iconbitmap('image/empty.ico')
		except Exception:
			pass
		# set title bar color (only on windows is working)
		self.set_title_bar_color()
		
		# set grid layout
		self.rowconfigure(list(range(MAIN_ROW)), weight = 1, uniform = 'a')
		self.columnconfigure(list(range(MAIN_COLUMN)), weight = 1, uniform = 'a')
		
		# set data
		self.formula_string = ttk.StringVar(value = '')
		self.result_string = ttk.StringVar(value = '0')
		self.display_nums: list[int] = []
		self.full_operation: list[int] = []
		
		# style
		
		self.Style = ttk.Style()
		self.Style.configure(
				'Result.TLabel',
				font = (FONT, OUTPUT_FONT_SIZE),
				borderwidth = 0,
				)
		
		self.Style.configure(
				'Formula.TLabel',
				font = (FONT, NORMAL_FONT_SIZE),
				borderwidth = 0,
				)
		
		self.Style.configure(
				'Number.TButton',
				font = (FONT, NORMAL_FONT_SIZE),
				borderwidth = 0,
				background = '#4c9be8'
				)
		
		self.Style.configure(
				'Operator.TButton',
				font = (FONT, NORMAL_FONT_SIZE),
				borderwidth = 0,
				background = '#4E5D6C',
				)
		
		self.Style.configure(
				'Symbol.TButton',
				font = (FONT, NORMAL_FONT_SIZE),
				borderwidth = 0,
				background = '#F0AD4E',
				)
		
		# set widgets label
		self.create_labels()
		
		# set widget buttons and operators
		self.num_buttons()
		self.math_symbols()
		self.math_operators()
		
		self.mainloop()
	
	def set_title_bar_color(self) -> None:
		"""
It set the color for title bar, it works only in windows.
		"""
		try:
			HWND = windll.user32.GetParent(self.winfo_id())
			DWMWA_ATTRIBUTE: int = 35
			TITLE_BAR_COLOR: int = 0x004C3720
			windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(TITLE_BAR_COLOR)), sizeof(c_int))
		except Exception:
			pass
	
	def create_labels(self) -> None:
		"""
		Creating the formula and result labels.

		"""
		# Formula Label
		OutputLabel(
				parent = self,
				row = 0,
				anchor = 'SE',
				style = 'Formula.TLabel',
				string_var = self.formula_string
				)
		# Result Label
		OutputLabel(
				parent = self,
				row = 1,
				anchor = 'E',
				style = 'Result.TLabel',
				string_var = self.result_string
				
				)
	
	def num_buttons(self) -> None:
		"""
Creating the number buttons, from 0 to 9 and the '.'.
		"""
		for number, data in NUMBER_POSITIONS.items():
			NumberButtons(
					parent = self,
					text = number,
					style = 'Number.TButton',
					func = self.num_press,
					row = data['row'],
					column = data['column'],
					span = data['span'],
					)
	
	def math_symbols(self) -> None:
		"""
Creating the symbols, +, —, = and /

		"""
		for data, symbol in MATH_POSITIONS.items():
			NumberButtons(
					parent = self,
					text = symbol['text'],
					style = 'Symbol.TButton',
					row = symbol['row'],
					column = symbol['column'],
					span = symbol['span'],
					func = self.math_press
					)
	
	def math_operators(self) -> None:
		"""
		Adding the math operators: cleaning, percent and invert
		"""
		
		# AC button
		Button(
				parent = self,
				text = MATH_OPERATORS['clear']['text'],
				style = 'Operator.TButton',
				func = self.clear,
				row = MATH_OPERATORS['clear']['row'],
				column = MATH_OPERATORS['clear']['column'],
				span = MATH_OPERATORS['clear']['span'],
				
				)
		# Invert button
		Button(
				parent = self,
				text = MATH_OPERATORS['invert']['text'],
				style = 'Operator.TButton',
				func = self.invert,
				row = MATH_OPERATORS['invert']['row'],
				column = MATH_OPERATORS['invert']['column'],
				span = MATH_OPERATORS['invert']['span'],
				)
		# Percent button
		Button(
				parent = self,
				text = MATH_OPERATORS['percent']['text'],
				style = 'Operator.TButton',
				func = self.percent,
				row = MATH_OPERATORS['percent']['row'],
				column = MATH_OPERATORS['percent']['column'],
				span = MATH_OPERATORS['percent']['span'],
				)
	
	# 	math logic
	def num_press(self, number: str) -> None:
		"""
		The logic for pressing a number, it set the label result and store the value in display_num.

		:param number:
		"""
		self.display_nums.append(number)
		full_number = ''.join(self.display_nums)
		self.result_string.set(full_number)
	
	def invert(self) -> None:
		"""
		The Invert logic, add a '-' to the display_nums if is positive else it will remove it from the list.

		"""
		current_number = ''.join(self.display_nums)
		if current_number:
			if float(current_number) > 0:
				self.display_nums.insert(0, '-')
			else:
				del self.display_nums[0]
			self.result_string.set(''.join(self.display_nums))
	
	def percent(self) -> None:
		"""
		The percent logic, just divide the number to 100 if is there.

		"""
		current_number = ''.join(self.display_nums)
		if current_number != '':
			percentage = float(current_number) / 100
			self.display_nums = list(str(percentage))
			self.result_string.set(''.join(self.display_nums))
	
	def clear(self) -> None:
		"""
		Clear the labels and the lists.

		"""
		self.result_string.set('0')
		
		self.formula_string.set('')
		self.display_nums.clear()
		self.full_operation.clear()
	
	def math_press(self, symbol: int) -> None:
		"""
		The math logic, take the full operation and put into an eval() function.And modifying the label and the list.

		:param symbol:
		"""
		current_number: str = ''.join(self.display_nums)
		try:
			if current_number:
				self.full_operation.append(current_number)
				if symbol != '=':
					self.full_operation.append(symbol)
					self.display_nums.clear()
					self.result_string.set('')
					self.formula_string.set(''.join(self.full_operation))
				else:
					formula = ' '.join(self.full_operation)
					result = eval(formula)
					if isinstance(result, float):
						if result.is_integer():
							result = int(result)
						else:
							result = round(result, 5)
					
					# update the lists
					self.full_operation.clear()
					self.display_nums = list(str(result))
					
					# update the label with the new numbers
					self.result_string.set(result)
					self.formula_string.set(formula)
		
		except ZeroDivisionError:
			self.result_string.set('Invalid!')
			self.display_nums.clear()
			
			self.formula_string.set('')
			self.full_operation.clear()


CalculatorApp()
