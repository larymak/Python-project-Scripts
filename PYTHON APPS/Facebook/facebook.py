import csv
import datetime
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkcalendar import Calendar

root = Tk()
root.title("Facebook Inc.")
root.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

# Initial Frame.
myFrame = LabelFrame(root, padx=70, pady=70, text="Welcome to Facebook", font=("Roboto", 15), fg="#1877F2")
myFrame.pack(padx=50, pady=25)

# Login and Sign Up Buttons.
loginButton = Button(myFrame, text="Login", padx=30, pady=10, font=("Roboto", 12))
Label(myFrame, text="OR", font="Roboto", fg="#1877F2")
signButton = Button(myFrame, text="Sign Up", padx=30, pady=10, font=("Roboto", 12))

user_email = None
l1_info = {}
l2_info = {}

psfilepath = []
psImage = None
images = []
title_label = Label()
image_label = Label()
description_label = Label()
button_forward = Button()
button_back = Button()

psfilepath1 = []
psImage1 = None
images1 = []
title_label1 = Label()
image_label1 = Label()
description_label1 = Label()
button_forward1 = Button()
button_back1 = Button()

psfilepath2 = []
psImage2 = None
images2 = []
title_label2 = Label()
image_label2 = Label()
description_label2 = Label()
button_forward2 = Button()
button_back2 = Button()

l3_info = {}
lpb = Button()
pl1 = Label()
friend_to_add = Entry()
l4_info = {}
button_comment = Button()
name_label = Label()
friend_request = []
request_to_accept = Entry()
request_to_reject = Entry()
l5_info = {}
acl = Label()
adl = Label()
ta = Button()
la = Button()
ta_info = {}
la_info = {}


class Post:

    post_id = 0

    def __init__(self):
        self.post_id = None
        self.post_type = None
        self.post_title = None
        self.post_description = None
        self.post_time = None
        self.post_date = None
        self.post_notification = 0
        self.post_recipients = 0
        self.privacy_id = 0
        self.page_id = None
        self.file_path = None

    @staticmethod
    def comment_on_a_post(post_id, u_id, u_obj):
        commenting = Toplevel()
        commenting.title("Comment")
        commenting.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        pc_frame = LabelFrame(commenting, text="Add Comment", font=("Roboto", 15), fg="#1877F2", padx=40, pady=20)
        pc_frame.grid(row=0, column=0, sticky="W", padx=20, pady=20)

        def add_comment_now(chosen_post_id, c_id, user_obj, ci):

            page_post_id = None
            is_page_post = False
            with open("Posts.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == chosen_post_id and row[12]:
                        is_page_post = True
                        page_post_id = row[12]
                        break

            if is_page_post:

                access = False
                with open("Page_Members.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[1] == str(user_obj.ID) and row[0] == page_post_id:
                            access = True

                with open("Pages.csv.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(user_obj.ID) and row[3] == page_post_id:
                            access = True

                if access:
                    # Creating comment object.
                    comment = Comment()
                    # Setting attributes.
                    comment.receiver_id, comment.chosen_post_id = c_id, chosen_post_id
                    comment.content, comment.sender_id = ci, user_obj.ID
                    comment.sender_first_name, comment.sender_last_name = user_obj.first_name, user_obj.last_name
                    # Storing comment data into a csv file.
                    with open("Comments.csv", "a", newline="") as data_file:
                        csv_writer = csv.writer(data_file, delimiter=",")
                        csv_writer.writerow(
                            [comment.receiver_id, comment.chosen_post_id, comment.content, comment.sender_id,
                             comment.sender_first_name, comment.sender_last_name, comment.pending])
                    Label(pc_frame, text="Comment Added.", font=("Roboto", 15), padx=7,
                          relief="groove").grid(row=2, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                    # Back.
                    Button(pc_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: commenting.destroy()).grid(row=3, column=0, pady=5, sticky="W")
                else:
                    Label(pc_frame, text="You can't comment on this post.", font=("Roboto", 15), padx=7,
                          relief="groove").grid(row=2, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                    # Back.
                    Button(pc_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: commenting.destroy()).grid(row=3, column=0, pady=5, sticky="W")
            else:
                # Creating comment object.
                comment = Comment()
                # Setting attributes.
                comment.receiver_id, comment.chosen_post_id = c_id, chosen_post_id
                comment.content, comment.sender_id = ci, user_obj.ID
                comment.sender_first_name, comment.sender_last_name = user_obj.first_name, user_obj.last_name
                # Storing comment data into a csv file.
                with open("Comments.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow(
                        [comment.receiver_id, comment.chosen_post_id, comment.content, comment.sender_id,
                         comment.sender_first_name, comment.sender_last_name, comment.pending])
                Label(pc_frame, text="Comment Added.", font=("Roboto", 15), padx=7,
                      relief="groove").grid(row=2, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                # Back.
                Button(pc_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: commenting.destroy()).grid(row=3, column=0, pady=5, sticky="W")

        Label(pc_frame, text="Enter Comment: ", font=("Roboto", 15), padx=7). \
            grid(row=0, column=0, columnspan=2, padx=4, pady=5, sticky="W")

        comment_input = Entry(pc_frame, highlightthickness=2)
        comment_input.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        comment_input.grid(row=0, column=2, pady=5, sticky="E")

        Button(pc_frame, text="Add", font=("Roboto", 14), width=9, fg="#1877F2",
               command=lambda: add_comment_now(post_id, u_id, u_obj, comment_input.get())).\
            grid(row=1, column=0, columnspan=3, pady=7, sticky="W")


class Comment:
    def __init__(self):
        self.receiver_id = None
        self.chosen_post_id = None
        self.content = None
        self.sender_id = None
        self.sender_first_name = None
        self.sender_last_name = None
        self.pending = True


class Friend:

    def __init__(self):

        self.first_name = None
        self.last_name = None
        self.pending = True


class Message:
    def __init__(self):
        self.receiver_ID = None
        self.sender_ID = None
        self.sender_first_name = None
        self.sender_last_name = None
        self.content = None
        self.pending = True


class Page:

    page_id = 0

    def __init__(self):
        self.page_id = None
        self.name = None
        self.category = None
        self.description = None
        self.creation_date = None
        self.users_who_liked = []


class User:

    users_id = 0
    privacy_lst_id = 0

    def __init__(self):

        self.first_name, self.last_name = None, None
        self.__email_or_phone = None
        self.__password = None
        self.ID = None
        self.gender, self.dob, self.about, self.current_city = None, None, None, None
        self.Education, self.Workplace, self.Relationship_Status = None, None, None
        self.online_status = False
        self.account_privacy = False

    def sign_up(self):
        top3 = Toplevel()
        top3.title("Sign up")
        top3.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        my_frame4 = LabelFrame(top3, text="Sign Up", font=("Roboto", 15), fg="#1877F2", padx=50, pady=40)
        my_frame4.pack(padx=20, pady=20)

        user_obj = self

        def clicked():

            email_phone = enter_email_phone.get()
            global user_email
            user_email = email_phone

            # Making sure the same email address or phone number isn't registered twice.
            repetition = False
            with open("Users_Database.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == email_phone:
                        repetition = True
                        break

            if repetition:

                def login_instead(obj):
                    top3.destroy()
                    obj.login()

                Label(my_frame4, text="Account already registered.", font=("Roboto", 13), relief="groove").\
                    grid(row=2, column=0, columnspan=2, sticky="W")
                Label(my_frame4, text="Login instead!", font=("Roboto", 13), relief="groove"). \
                    grid(row=3, column=0, columnspan=2, sticky="W")
                Button(my_frame4, text="Login", font=("Roboto", 13), width=12, bg="#1877F2", fg="white",
                       command=lambda: login_instead(user_obj)).grid(row=4, column=0, columnspan=2, pady=12, sticky="W")

            else:
                top3.destroy()
                top4 = Toplevel()
                top4.title("Sign Up")
                top4.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

                my_frame5 = LabelFrame(top4, text="Sign Up", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
                my_frame5.pack(padx=20, pady=20)

                Label(my_frame5, text="Password", font=("Roboto", 15), padx=7). \
                    grid(row=0, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                Label(my_frame5, text="First Name", font=("Roboto", 15), padx=7). \
                    grid(row=1, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                Label(my_frame5, text="Last Name", font=("Roboto", 15), padx=7). \
                    grid(row=2, column=0, columnspan=2, padx=4, pady=5, sticky="W")
                Label(my_frame5, text="Gender", font=("Roboto", 15), padx=7).\
                    grid(row=3, column=0, columnspan=2, padx=4, pady=(5, 0), sticky="W")
                Label(my_frame5, text="Date of Birth", font=("Roboto", 15), padx=7). \
                    grid(row=5, column=0, columnspan=2, padx=4, pady=5, sticky="W")

                user_password = Entry(my_frame5, highlightthickness=2)
                user_password.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_first_name = Entry(my_frame5, highlightthickness=2)
                user_first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_last_name = Entry(my_frame5, highlightthickness=2)
                user_last_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

                user_gender = StringVar()
                user_gender.set("Male")
                Radiobutton(my_frame5, text="Male", variable=user_gender, font=("Helvetica 18 bold", 12),
                            value="Male", fg="#1877F2").grid(row=4, column=0, pady=5, sticky="W")
                Radiobutton(my_frame5, text="Female", variable=user_gender, font=("Helvetica 18 bold", 12),
                            value="Female", fg="#1877F2").grid(row=4, column=1, pady=5, sticky="W")
                Radiobutton(my_frame5, text="Other", variable=user_gender, font=("Helvetica 18 bold", 12),
                            value="Other", fg="#1877F2").grid(row=4, column=2, pady=5, sticky="W")

                cal = Calendar(my_frame5, selectmode='day', year=2020, month=5, day=22)
                cal.grid(row=6, column=2, pady=5, sticky="E", padx=15)

                user_password.grid(row=0, column=2, pady=5, sticky="E")
                user_first_name.grid(row=1, column=2, pady=5, sticky="E")
                user_last_name.grid(row=2, column=2, pady=5, sticky="E")

                l1 = Label(my_frame5, text="*Required field(s)\nempty.", font=("Helvetica 18 bold", 13),
                           padx=20, pady=4, bd=1, relief="groove", fg="#FF0000")

                def sign_up_now():

                    global l1_info

                    if user_password.index("end") == 0 or user_first_name.index("end") == 0 or user_last_name.\
                            index("end") == 0:
                        l1.grid(row=8, column=0, columnspan=2, pady=5, padx=3, sticky="W")
                        l1_info = l1.grid_info()
                    else:
                        if l1_info != {}:
                            if l1_info["row"] == 8:
                                l1.destroy()
                        # Setting object's attributes after data has been entered.
                        self.__email_or_phone = user_email
                        self.__password = user_password.get()
                        self.first_name = user_first_name.get()
                        self.last_name = user_last_name.get()
                        self.dob = cal.get_date()
                        self.gender = user_gender.get()

                        # Each user gets a unique user id.
                        r = csv.reader(open("Users_Database.csv"))
                        lines = list(r)
                        for lst in range(1, len(lines)):
                            if lines[lst][0]:
                                User.users_id = lines[lst][0]
                        self.ID = int(User.users_id) + 1

                        with open("Users_Database.csv", "a", newline="") as user_data:
                            csv_writer = csv.writer(user_data, delimiter=",")
                            csv_writer.writerow(
                                [self.ID, self.first_name, self.last_name, self.__email_or_phone, self.__password,
                                 self.gender, self.dob, self.about, self.current_city, self.Education,
                                 self.Workplace, self.Relationship_Status, self.account_privacy])

                        # Signed in notification.
                        Label(my_frame5, text="You're signed in!", font=("Roboto", 15)). \
                            grid(row=8, column=0, columnspan=2, pady=5, padx=3, sticky="W")

                        def login_after_signup(obj):
                            top4.destroy()
                            obj.login()

                        def exit_window():
                            top4.destroy()

                        # Actions to take after profile has been created.
                        Button(my_frame5, text="Login", font=("Roboto", 14), width=10, bg="#1877F2", fg="white",
                               command=lambda: login_after_signup(user_obj)).grid(row=9, column=0, columnspan=2, pady=5,
                                                                                  sticky="W")
                        Button(my_frame5, text="Exit", font=("Roboto", 14), width=10, fg="#1877F2",
                               command=exit_window).grid(row=9, column=2, pady=5, sticky="W")

                Button(my_frame5, text="Enter", font=("Roboto", 14), width=9, fg="#1877F2", command=sign_up_now).\
                    grid(row=7, column=0, columnspan=3, pady=7, sticky="W")

        my_label = Label(my_frame4, text="Email Address", font=("Roboto", 13), padx=20, pady=4, bd=1, relief="sunken")
        my_button = Button(my_frame4, text="Enter", font=("Roboto", 13), width=7, padx=2, fg="#1877F2", command=clicked)
        enter_email_phone = Entry(my_frame4, highlightthickness=2)
        enter_email_phone.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

        my_label.grid(row=0, column=0, padx=7, sticky="W")
        my_button.grid(row=1, column=0, pady=12, sticky="W")
        enter_email_phone.grid(row=0, column=1, sticky="E")

    def login(self):

        user_obj = self

        top = Toplevel()
        top.title("Login")
        top.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        my_frame2 = LabelFrame(top, text="Login", font=("Roboto", 15), fg="#1877F2", padx=50, pady=40)
        my_frame2.pack(padx=30, pady=30)

        def info_entered():
            email_phone = enter_email_phone.get()
            password = enter_password.get()

            registered = False
            with open("Users_Database.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == email_phone:
                        self.ID, self.first_name, self.last_name = row[0], row[1], row[2]
                        self.__email_or_phone, self.__password = row[3], row[4]
                        self.gender, self.dob, self.about, self.current_city = row[5], row[6], row[7], row[8]
                        self.Education, self.Workplace, self.Relationship_Status = row[9], row[10], row[11]
                        self.account_privacy = row[12]
                        registered = True
                        break

            if registered:
                match = False
                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[3] == email_phone and row[4] == password:
                            match = True
                            break

                if match:
                    Label(my_frame2, text="You are Logged in!", font=("Roboto", 12)).grid(row=3, column=0, columnspan=2,
                                                                                          sticky="W")
                    # Creating user's home page.
                    top.destroy()
                    home = Toplevel()
                    home.title("Home Page")
                    home.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

                    def see_messages(obj):
                        obj.see_user_messages()

                    def see_friends(obj):
                        obj.view_user_friends()

                    # Displaying user's profile information.
                    profile_info = LabelFrame(home, text="Profile Info", font=("Roboto", 15), fg="#1877F2", padx=20,
                                              pady=10)
                    profile_info.grid(row=0, column=0, padx=20, pady=20, sticky="W")

                    Label(profile_info, text=self.first_name + " " + self.last_name, font=("Roboto", 14)).\
                        grid(row=0, column=0, pady=5, sticky="W")

                    Label(profile_info, text="About:", font=("Roboto", 12)).grid(row=1, column=0, pady=3, sticky="W")
                    Label(profile_info, text=self.about, font=("Helvetica", 12)).grid(row=1, column=1, pady=3,
                                                                                      sticky="W")
                    Label(profile_info, text="Current City: ", font=("Roboto", 12)).grid(row=2, column=0,  pady=3,
                                                                                         sticky="W")
                    Label(profile_info, text=self.current_city, font=("Helvetica", 12)).grid(row=2, column=1, pady=3,
                                                                                             sticky="W")
                    Label(profile_info, text="Education: ", font=("Roboto", 12)).grid(row=3, column=0, pady=3,
                                                                                      sticky="W")
                    Label(profile_info, text=self.Education, font=("Helvetica", 12)).grid(row=3, column=1,  pady=3,
                                                                                          sticky="W")
                    Label(profile_info, text="Workplace: ", font=("Roboto", 12)).grid(row=4, column=0, pady=3,
                                                                                      sticky="W")
                    Label(profile_info, text=self.Workplace, font=("Helvetica", 12)).grid(row=4, column=1,  pady=3,
                                                                                          sticky="W")
                    Label(profile_info, text="Relationship Status: ", font=("Roboto", 12)).grid(row=5, column=0, pady=3,
                                                                                                sticky="W")
                    Label(profile_info, text=self.Relationship_Status, font=("Helvetica", 12)).grid(row=5, column=1,
                                                                                                    pady=3, sticky="W")

                    # Displaying user's posts.
                    profile_posts = LabelFrame(home, text="Posts", font=("Roboto", 15), fg="#1877F2", padx=30, pady=10)
                    profile_posts.grid(row=1, column=0, padx=20, pady=20, sticky="W")

                    pstitle = []
                    psdescription = []
                    global psfilepath
                    global psImage
                    global images
                    global title_label
                    global image_label
                    global description_label
                    global button_forward
                    global button_back
                    images.clear()
                    psfilepath.clear()

                    post_num = 1

                    has_posts = False
                    with open("Posts.csv") as data_file:
                        csv_reader = csv.reader(data_file, delimiter=",")
                        for row in csv_reader:
                            if row[0] == self.ID and not row[12]:
                                pstitle.append(row[5])
                                psdescription.append(row[6])
                                psfilepath.append(row[13])
                                has_posts = True

                    if has_posts:
                        for pic in psfilepath:
                            my_pic = Image.open(pic)
                            resized = my_pic.resize((320, 220))
                            new_pic = ImageTk.PhotoImage(resized)
                            images.append(new_pic)

                        title_label = Label(profile_posts, text=pstitle[post_num-1], font=("Roboto", 13), padx=7,
                                            pady=5)
                        image_label = Label(profile_posts, image=images[post_num-1])
                        description_label = Label(profile_posts, text=psdescription[post_num-1],
                                                  font=("Helvetica bold 18", 13), padx=7, pady=3)

                        def forward(p_num):
                            global title_label
                            global image_label
                            global description_label
                            global button_forward
                            global button_back
                            global images

                            title_label.grid_forget()
                            image_label.grid_forget()
                            description_label.grid_forget()

                            title_label = Label(profile_posts, text=pstitle[p_num - 1], font=("Roboto", 13), padx=7,
                                                pady=5)
                            image_label = Label(profile_posts, image=images[p_num - 1])
                            description_label = Label(profile_posts, text=psdescription[p_num - 1],
                                                      font=("Helvetica bold 18", 13), padx=7, pady=3)

                            button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                    fg="#1877F2", command=lambda: forward(p_num+1))
                            button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: back(p_num-1))

                            if p_num == len(images):
                                button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                        state="disabled")

                            title_label.grid(row=0, column=0, sticky="W")
                            image_label.grid(row=1, column=0, columnspan=2, sticky="W")
                            description_label.grid(row=2, column=0, sticky="W", pady=7)
                            button_forward.place(x=250, y=295)
                            button_back.grid(row=3, column=0, sticky="W")

                        def back(p_num):
                            global title_label
                            global image_label
                            global description_label
                            global button_forward
                            global button_back
                            global images

                            title_label.grid_forget()
                            image_label.grid_forget()
                            description_label.grid_forget()

                            title_label = Label(profile_posts, text=pstitle[p_num - 1], font=("Roboto", 13), padx=7,
                                                pady=5)
                            image_label = Label(profile_posts, image=images[p_num - 1])
                            description_label = Label(profile_posts, text=psdescription[p_num - 1],
                                                      font=("Helvetica bold 18", 13), padx=7, pady=3)

                            button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                    fg="#1877F2", command=lambda: forward(p_num + 1))
                            button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: back(p_num - 1))

                            if p_num == 1:
                                button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13),
                                                     state="disabled")

                            title_label.grid(row=0, column=0, sticky="W")
                            image_label.grid(row=1, column=0, columnspan=2, sticky="W")
                            description_label.grid(row=2, column=0, sticky="W", pady=7)
                            button_forward.place(x=250, y=295)
                            button_back.grid(row=3, column=0, sticky="W")

                        if len(images) != 1:
                            button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                    fg="#1877F2", command=lambda: forward(post_num + 1))
                            button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: back(post_num))
                        else:
                            button_forward = Button(profile_posts, text=">>", width=6, font=("Roboto", 13),
                                                    fg="#1877F2", state="disabled")
                            button_back = Button(profile_posts, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 state="disabled")

                        title_label.grid(row=0, column=0, sticky="W")
                        image_label.grid(row=1, column=0, columnspan=2, sticky="W")
                        description_label.grid(row=2, column=0, sticky="W", pady=7)
                        button_forward.place(x=250, y=295)
                        button_back.grid(row=3, column=0, sticky="W")

                    if not has_posts:

                        Label(profile_posts, text="You've no posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3,
                                                                                                sticky="W")

                    # Displaying user's messages.
                    see = LabelFrame(home, text="See", font=("Roboto", 15), fg="#1877F2", padx=30, pady=10)
                    see.grid(row=0, column=1, padx=15, pady=5, sticky="E")

                    Button(see, text="Messages", width=14, font=("Roboto", 13), command=lambda:
                           see_messages(user_obj)).grid(row=0, column=0, pady=4, sticky="W")
                    Button(see, text="Friends", width=14, font=("Roboto", 13), command=lambda: see_friends(user_obj)). \
                        grid(row=1, column=0, pady=4, sticky="W")

                    def edit_profile(obj):
                        obj.edit_user()

                    def change_privacy(obj):
                        obj.change_account_privacy()

                    def block(obj):
                        obj.block_a_user()

                    def unblock(obj):
                        obj.unblock_a_user()

                    def account_privacy():
                        privacy = Toplevel()
                        privacy.title("Privacy Settings")
                        privacy.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

                        pr_frame = LabelFrame(privacy, text="Privacy Settings", font=("Roboto", 15), fg="#1877F2",
                                              padx=50, pady=30)
                        pr_frame.pack(padx=20, pady=20)

                        # Change account privacy.
                        Button(pr_frame, text="Privacy", width=14, font=("Roboto", 13),
                               command=lambda: change_privacy(user_obj)).grid(row=0, column=0, pady=5, sticky="W")
                        # Block a user.
                        Button(pr_frame, text="Block User", width=14, font=("Roboto", 13),
                               command=lambda: block(user_obj)).grid(row=1, column=0, pady=5, sticky="W")
                        # Unblock a user.
                        Button(pr_frame, text="Unblock User", width=14, font=("Roboto", 13),
                               command=lambda: unblock(user_obj)).grid(row=2, column=0, pady=5, sticky="W")
                        # Back.
                        Button(pr_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                               command=lambda: privacy.destroy()).grid(row=5, column=0, pady=5, sticky="W")

                    def delete_profile(obj):
                        obj.delete_user()
                        home.destroy()

                    def settings():
                        # Settings window.
                        setting = Toplevel()
                        setting.title("Settings")
                        setting.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

                        set_frame = LabelFrame(setting, text="Settings", font=("Roboto", 15), fg="#1877F2", padx=50,
                                               pady=30)
                        set_frame.pack(padx=40, pady=40)

                        # Edit profile.
                        Button(set_frame, border=1, text="Edit Profile", width=14, font=("Roboto", 13),
                               command=lambda: edit_profile(user_obj)).grid(row=0, column=0, pady=5, sticky="W")
                        # Change account privacy.
                        Button(set_frame, text="Account Privacy", width=14, font=("Roboto", 13),
                               command=account_privacy).grid(row=1, column=0, pady=5, sticky="W")
                        # Delete profile.
                        Button(set_frame, text="Delete Profile", width=14, font=("Roboto", 13), fg="#1877F2",
                               command=lambda: delete_profile(user_obj)).grid(row=2, column=0, pady=5, sticky="W")
                        # Back.
                        Button(set_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                               command=lambda: setting.destroy()).grid(row=3, column=0, pady=5, sticky="W")

                    def search_a_user(obj):
                        obj.search_user()

                    def search_a_page(obj):
                        obj.search_page()

                    def send_request(obj):
                        obj.add_friend()

                    def send_message(obj):
                        obj.send_message()

                    def log_out(obj):
                        obj.logout()
                        home.destroy()

                    def create_post(obj):
                        obj.create_a_post()

                    def create_page(obj):
                        obj.create_a_page()

                    def search():
                        # Search window.
                        search_window = Toplevel()
                        search_window.title("Search")
                        search_window.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

                        search_frame = LabelFrame(search_window, text="Search", font=("Roboto", 15), fg="#1877F2",
                                                  padx=50, pady=30)
                        search_frame.pack(padx=20, pady=20)

                        # Search a user's profile.
                        Button(search_frame, text="Search User", width=14, font=("Roboto", 13),
                               command=lambda: search_a_user(user_obj)).grid(row=0, column=0, pady=5, sticky="W")
                        # Search a page.
                        Button(search_frame, text="Search Page", width=14, font=("Roboto", 13),
                               command=lambda: search_a_page(user_obj)).grid(row=1, column=0, pady=5, sticky="W")
                        # Back.
                        Button(search_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                               command=lambda: search_window.destroy()).grid(row=2, column=0, pady=5, sticky="W")

                    # Displaying all the options.
                    options = LabelFrame(home, text="Do", font=("Roboto", 15), fg="#1877F2", padx=30, pady=10)
                    options.grid(row=1, column=1, padx=15, pady=15, sticky="E")

                    Button(options, text="Settings", width=14, font=("Roboto", 13), command=settings). \
                        grid(row=0, column=0, pady=4, sticky="W")
                    Button(options, text="Search", width=14, font=("Roboto", 13), command=search). \
                        grid(row=1, column=0, pady=2, sticky="W")
                    Button(options, text="Send Request", width=14, font=("Roboto", 13),
                           command=lambda: send_request(user_obj)).grid(row=2, column=0, pady=4, sticky="W")
                    Button(options, text="Send Message", width=14, font=("Roboto", 13),
                           command=lambda: send_message(user_obj)).grid(row=3, column=0, pady=4, sticky="W")
                    Button(options, text="Logout", width=14, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: log_out(user_obj)).grid(row=4, column=0, pady=4, sticky="W")

                    # Displaying creating options.
                    create = LabelFrame(home, text="Create", font=("Roboto", 15), fg="#1877F2", padx=30, pady=10)
                    create.grid(row=0, column=2, padx=20, pady=20, sticky="W")

                    Button(create, text="Post", width=14, font=("Roboto", 13), command= lambda: create_post(user_obj)).\
                        grid(row=0, column=0, pady=4, sticky="W")
                    Button(create, text="Page", width=14, font=("Roboto", 13), command= lambda: create_page(user_obj)).\
                        grid(row=1, column=0, pady=4, sticky="W")

                    self.online_status = True

                    self.accept_decline_friend_request()

                else:

                    def password_reset(obj):
                        top.destroy()
                        obj.user_update()

                    def login_again(obj):
                        top.destroy()
                        obj.login()

                    Label(my_frame2, text="Incorrect Information!", font=("Roboto", 13)).\
                        grid(row=4, column=0, columnspan=2, pady=5)
                    reset_button = Button(my_frame2, text="Reset Password", width=15, font=("Roboto", 13), fg="#1877F2",
                                          command=lambda: password_reset(user_obj))
                    try_button = Button(my_frame2, text="Try again", width=13, font=("Roboto", 13), fg="#1877F2",
                                        command=lambda: login_again(user_obj))

                    reset_button.grid(row=5, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                    Label(my_frame2, text="OR", font=("Roboto", 13)).grid(row=6, column=0, columnspan=2, pady=5)
                    try_button.grid(row=7, column=0, columnspan=2, padx=3, sticky="W")

            else:
                Label(my_frame2, text="Sign Up First!", font=("Roboto", 13)).grid(row=4, column=0, columnspan=2, pady=5)
                sign_up_button = Button(my_frame2, text="Sign Up", width=14, font=("Roboto", 13), fg="#1877F2")
                exit_button = Button(my_frame2, text="Exit", width=14, font=("Roboto", 13), fg="#1877F2")

                sign_up_button.grid(row=5, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                Label(my_frame2, text="OR", font=("Roboto", 12)).grid(row=6, column=0, columnspan=2)
                exit_button.grid(row=7, column=0, columnspan=2, padx=3, sticky="W")

        my_label1 = Label(my_frame2, text="Email or Phone", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken")
        my_label2 = Label(my_frame2, text="Password", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken")
        my_button = Button(my_frame2, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2", command=info_entered)

        enter_email_phone = Entry(my_frame2, highlightthickness=2)
        enter_email_phone.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        enter_password = Entry(my_frame2, highlightthickness=2)
        enter_password.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

        my_label1.grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")
        my_label2.grid(row=1, column=0, columnspan=2, padx=3, sticky="W")
        my_button.grid(row=2, column=0, pady=12, sticky="W")
        enter_email_phone.grid(row=0, column=2, sticky="E")
        enter_password.grid(row=1, column=2, sticky="E")

    def logout(self):
        self.online_status = False

    # Edit User's profile.
    def edit_user(self):
        edit = Toplevel()
        edit.title("Edit Profile")

        edit_frame = LabelFrame(edit, text="Edit Profile", font=("Roboto", 15), fg="#1877F2", padx=50, pady=40)
        edit_frame.pack(padx=20, pady=20)

        Label(edit_frame, text="About", font=("Roboto", 13), padx=7).grid(row=0, column=0, columnspan=2, pady=5,
                                                                          sticky="W")
        Label(edit_frame, text="City", font=("Roboto", 13), padx=7).grid(row=1, column=0, columnspan=2, pady=5,
                                                                         sticky="W")
        Label(edit_frame, text="Workplace", font=("Roboto", 13), padx=7).grid(row=2, column=0, columnspan=2, pady=5,
                                                                              sticky="W")
        Label(edit_frame, text="Education", font=("Roboto", 13), padx=7).grid(row=3, column=0, columnspan=2, pady=5,
                                                                              sticky="W")
        Label(edit_frame, text="Relationship Status", font=("Roboto", 13), padx=7).grid(row=4, column=0, columnspan=2,
                                                                                        pady=5, sticky="W")
        # Getting previous values.
        with open("Users_Database.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == str(self.ID):
                    about = row[7]
                    city = row[8]
                    ed = row[9]
                    wp = row[10]
                    rs = row[11]

        user_about = Entry(edit_frame, highlightthickness=2)
        user_about.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_about.insert(0, about)
        user_city = Entry(edit_frame, highlightthickness=2)
        user_city.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_city.insert(0, city)
        user_workplace = Entry(edit_frame, highlightthickness=2)
        user_workplace.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_workplace.insert(0, wp)
        user_education = Entry(edit_frame, highlightthickness=2)
        user_education.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_education.insert(0, ed)
        user_relationship = Entry(edit_frame, highlightthickness=2)
        user_relationship.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        user_relationship.insert(0, rs)

        user_about.grid(row=0, column=2, sticky="E")
        user_city.grid(row=1, column=2, sticky="E")
        user_workplace.grid(row=2, column=2, sticky="E")
        user_education.grid(row=3, column=2, sticky="E")
        user_relationship.grid(row=4, column=2, sticky="E")

        def edit_now():
            self.about = user_about.get()
            self.current_city = user_city.get()
            self.Workplace = user_workplace.get()
            self.Education = user_education.get()
            self.Relationship_Status = user_relationship.get()

            # Updating user's info in the database.
            r = csv.reader(open("Users_Database.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][0] == str(self.ID):
                    lines[lst][7], lines[lst][8], lines[lst][9] = self.about, self.current_city, self.Education
                    lines[lst][10], lines[lst][11] = self.Workplace, self.Relationship_Status
                    break
            writer = csv.writer(open("Users_Database.csv", "w", newline=""))
            writer.writerows(lines)
            Label(edit_frame, text="Profile Updated!", font=("Roboto", 14), pady=8).\
                grid(row=6, column=0, columnspan=2, pady=5, sticky="W")
            # Back.
            Button(edit_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                   command=lambda: edit.destroy()).grid(row=7, column=0, pady=3, sticky="W")

        Button(edit_frame, text="Done", font=("Roboto", 13), width=7, fg="#1877F2", command=edit_now).\
            grid(row=5, column=0, columnspan=3, sticky="W", pady=10)

    # View your posts.
    def view_user_posts(self):
        posts = []
        with open("Posts.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == self.ID and not row[12]:
                    posts.append(row[3])
        return posts

    def see_user_messages(self):
        pass

    # View your friends.
    def view_user_friends(self):
        seeing_friends = Toplevel()
        seeing_friends.title("See Friends")
        seeing_friends.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        sf_frame = LabelFrame(seeing_friends, text="Friends", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        sf_frame.grid(row=0, column=0, sticky="W", padx=20, pady=15)

        has_friends = False
        with open("Friends.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == str(self.ID) and row[6] == str(False):
                    has_friends = True
                elif row[3] == str(self.ID) and row[6] == str(False):
                    has_friends = True

        if has_friends:

            row_no = 0
            with open("Friends.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(self.ID) and row[6] == str(False):
                        Label(sf_frame, text=f"{row[4]} {row[5]}", font=("Roboto", 13), padx=20, pady=5,
                              bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=2, padx=3,
                                                          sticky="W")
                        row_no += 1
                    elif row[3] == str(self.ID) and row[6] == str(False):
                        Label(sf_frame, text=f"{row[1]} {row[2]}", font=("Roboto", 13), padx=20, pady=5,
                              bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=2, padx=3,
                                                          sticky="W")
                        row_no += 1
        else:
            Label(sf_frame, text="You've no friends.", font=("Roboto", 13), padx=20, pady=5,
                  bd=1, relief="groove").grid(row=0, column=0, columnspan=2, pady=2, padx=3,
                                              sticky="W")

    def set_account_privacy(self, value):
        self.account_privacy = value

    # Change your account privacy.
    def change_account_privacy(self):
        user_obj = self

        account_privacy = Toplevel()
        account_privacy.title("Account Privacy")
        account_privacy.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        ap_frame = LabelFrame(account_privacy, text="Change Account Privacy", font=("Roboto", 15), fg="#1877F2",
                              padx=50, pady=40)
        ap_frame.pack(padx=20, pady=20)

        def make_public(obj):
            obj.set_account_privacy(False)
            Label(ap_frame, text="Status Updated!", font=("Roboto", 13), padx=7). \
                grid(row=2, column=0, columnspan=2, pady=5, sticky="W")
            Button(ap_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                   command=lambda: account_privacy.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        def make_private(obj):
            obj.set_account_privacy(True)
            Label(ap_frame, text="Status Updated!", font=("Roboto", 13), padx=7). \
                grid(row=2, column=0, columnspan=2, pady=5, sticky="W")
            Button(ap_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                   command=lambda: account_privacy.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        if self.account_privacy == str(True):
            Label(ap_frame, text="Your account is private.", font=("Roboto", 13), padx=7).\
                grid(row=0, column=0, columnspan=2, pady=5, sticky="W")
            Button(ap_frame, text="Make Public", font=("Roboto", 13), width=14, fg="#1877F2",
                   command=lambda: make_public(user_obj)).grid(row=1, column=0, columnspan=2, padx=4,
                                                               pady=7, sticky="W")

        else:
            Label(ap_frame, text="Your account is public.", font=("Roboto", 13), padx=7). \
                grid(row=0, column=0, columnspan=2, pady=5, sticky="W")
            Button(ap_frame, text="Make Private", font=("Roboto", 13), width=14, fg="#1877F2",
                   command=lambda: make_private(user_obj)).grid(row=1, column=0, columnspan=2, padx=4,
                                                                pady=7, sticky="W")

        # Updating account privacy in the database.
        r = csv.reader(open("Users_Database.csv"))
        lines = list(r)
        for lst in range(len(lines)):
            if lines[lst][0] == str(self.ID):
                lines[lst][12] = self.account_privacy
                break
        writer = csv.writer(open("Users_Database.csv", "w", newline=""))
        writer.writerows(lines)

    # Update your password in the database.
    def user_update(self):
        user_obj = self

        update = Toplevel()
        update.title("Update Info.")
        update.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        up_frame = LabelFrame(update, text="Reset Password", font=("Roboto", 15), fg="#1877F2",
                             padx=50, pady=40)
        up_frame.pack(padx=20, pady=20)

        Label(up_frame, text="Email or Phone", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        email_phone = Entry(up_frame, highlightthickness=2)
        email_phone.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        email_phone.grid(row=0, column=2, sticky="E")

        def login_again(obj):
            update.destroy()
            obj.login()

        def try_again(obj):
            update.destroy()
            obj.user_update()

        def password_entered(new):
            self.__password = new

            # Updating user's password in the database.
            r = csv.reader(open("Users_Database.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][0] == str(self.ID):
                    lines[lst][4] = self.__password
                    break
            writer = csv.writer(open("Users_Database.csv", "w", newline=""))
            writer.writerows(lines)

            Label(up_frame, text="Password Updated!", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
                grid(row=3, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            Button(up_frame, text="Login", font=("Roboto", 13), width=12, fg="#1877F2",
                   command=lambda: login_again(user_obj)).grid(row=4, column=0, columnspan=3, pady=10, sticky="W")

        def info_entered():
            found = False
            with open("Users_Database.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == email_phone.get():
                        self.ID = row[0]
                        found = True

            if found:
                b1.destroy()

                Label(up_frame, text="Password", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
                    grid(row=1, column=0, columnspan=2, pady=10, padx=3, sticky="W")

                new_password = Entry(up_frame, highlightthickness=2)
                new_password.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                new_password.grid(row=1, column=2, sticky="E")

                Button(up_frame, text="Update", font=("Roboto", 13), width=7, fg="#1877F2",
                       command=lambda: password_entered(new_password.get())).grid(row=2, column=0, columnspan=3,
                                                                                  pady=5,
                                                                                  sticky="W")
            else:
                Label(up_frame, text="Incorrect Information. Try again!", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="sunken").grid(row=2, column=0, columnspan=2, pady=10, padx=3, sticky="W")

                Button(up_frame, text="Try Again", font=("Roboto", 13), width=12, fg="#1877F2",
                       command=lambda: try_again(user_obj)).grid(row=3, column=0, columnspan=3, pady=5, sticky="W")

        b1 = Button(up_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2", command=info_entered)
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def find_users(self, first_name):
        users = []
        # Finding all users with the first name that you searched for.
        with open("Users_Database.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[1] == first_name and row[0] != str(self.ID):
                    users.append(row[0])

        # Excluding those who've blocked you.
        with open("Blocked_Users.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[1] == str(self.ID) and row[0] in users:
                    users.remove(row[0])
        return users

    def search_user(self):
        search_user_win = Toplevel()
        search_user_win.title("Search User")
        search_user_win.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        s_frame = LabelFrame(search_user_win, text="Search a user", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        s_frame.pack(padx=20, pady=20)

        Label(s_frame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(s_frame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def search_now(user_ID, users, row_no):
            ID = users[user_ID - 1]
            # Checking if the user you are searching for hasn't blocked you.
            access = True
            with open("Blocked_Users.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == ID and row[1] == self.ID:
                        access = False
                        break
            if access:
                search_user_win.destroy()
                return self.display_user_profile(ID)
            else:
                Label(s_frame, text="Search Blocked.", font=("Roboto", 13), padx=20, pady=5). \
                    grid(row=row_no + 3, column=0, columnspan=3, pady=7, sticky="W")

        def info_entered(name):
            users = self.find_users(name)

            if users:
                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(s_frame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20, pady=5,
                                  bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10, padx=3,
                                                              sticky="W")
                            row_no += 1

                Label(s_frame, text="Number of profile\nyou want to see: ", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="sunken", fg="#1877F2").grid(row=row_no+1, column=0, columnspan=2, pady=10, padx=3,
                                                          sticky="W")

                user_to_see = Entry(s_frame, highlightthickness=2)
                user_to_see.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_see.grid(row=row_no+1, column=2, sticky="E")

                b2 = Button(s_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: search_now(int(user_to_see.get()), users, row_no))
                b2.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")

            else:
                Label(s_frame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="sunken", fg="#1877F2").grid(row=2, column=0, columnspan=2, pady=10, padx=3,
                                                          sticky="W")

        b1 = Button(s_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def delete_user(self):
        # Deleting user's account from the database.
        r = csv.reader(open("Users_Database.csv"))
        lines = list(r)
        for lst in range(len(lines)):
            if lines[lst][0] == str(self.ID):
                lines.remove(lines[lst])
                break
        writer = csv.writer(open("Users_Database.csv", "w", newline=""))
        writer.writerows(lines)
        print("Account deleted.")

    def block_a_user(self):
        block = Toplevel()
        block.title("Block")
        block.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        b_frame = LabelFrame(block, text="Block a User", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        b_frame.pack(padx=20, pady=20)

        Label(b_frame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(b_frame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def block_now(user_ID, users, row_no):
            id = users[user_ID - 1]
            # Checking if the user isn't already blocked.
            blocked = False
            with open("Blocked_Users.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == self.ID and row[1] == id:
                        blocked = True
                        break
            # Blocking the user.
            if not blocked:
                with open("Blocked_Users.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow([self.ID, id])
                Label(b_frame, text="User blocked.", font=("Roboto", 13), padx=20, pady=5).\
                    grid(row=row_no+3, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(b_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: block.destroy()).grid(row=row_no+4, column=0, pady=3, sticky="W")
            else:
                Label(b_frame, text="User is already blocked.", font=("Roboto", 13), padx=20, pady=5).\
                    grid(row=row_no+3, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(b_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: block.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")

        def info_entered(name):
            users = self.find_users(name)

            if users:

                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(b_frame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20,
                                  pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10,
                                                                      padx=3, sticky="W")
                            row_no += 1

                Label(b_frame, text="Number of profile\nyou want to block: ", font=("Roboto", 13), padx=20, pady=5,
                      bd=1, relief="sunken", fg="#1877F2").grid(row=row_no+1, column=0, columnspan=2, pady=10, padx=3,
                                                                sticky="W")

                user_to_block = Entry(b_frame, highlightthickness=2)
                user_to_block.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_block.grid(row=row_no+1, column=2, sticky="E")

                b2 = Button(b_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: block_now(int(user_to_block.get()), users, row_no))
                b2.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")

            else:
                Label(b_frame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, relief="groove"). \
                    grid(row=2, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(b_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: block.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(b_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def unblock_a_user(self):
        unblock = Toplevel()
        unblock.title("Unblock")
        unblock.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        ub_frame = LabelFrame(unblock, text="Unblock a User", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        ub_frame.pack(padx=20, pady=20)

        Label(ub_frame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(ub_frame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def unblock_now(user_ID, users, row_no):
            ID = users[user_ID - 1]
            # Unblocking the user if blocked.
            blocked_user = False
            r = csv.reader(open("Blocked_Users.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][0] == str(self.ID) and lines[lst][1] == ID:
                    blocked_user = True
                    lines.remove(lines[lst])
            writer = csv.writer(open("Blocked_Users.csv", "w", newline=""))
            writer.writerows(lines)
            # If the user wasn't blocked.
            if not blocked_user:
                Label(ub_frame, text="You've not blocked this user.", font=("Roboto", 13), padx=20, pady=5).\
                    grid(row=row_no+3, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(ub_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: unblock.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")
            else:
                Label(ub_frame, text="User unblocked.", font=("Roboto", 13), padx=20, pady=5).\
                    grid(row=row_no+3, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(ub_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: unblock.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")

        def info_entered(name):
            users = self.find_users(name)

            if users:

                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(ub_frame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20,
                                  pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10,
                                                                      padx=3, sticky="W")
                            row_no += 1

                Label(ub_frame, text="Number of profile\nyou want to unblock: ", font=("Roboto", 13), padx=20, pady=5,
                      bd=1, relief="sunken", fg="#1877F2").grid(row=row_no+1, column=0, columnspan=2, pady=10, padx=3,
                                                                sticky="W")

                user_to_unblock = Entry(ub_frame, highlightthickness=2)
                user_to_unblock.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_unblock.grid(row=row_no+1, column=2, sticky="E")

                b2 = Button(ub_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: unblock_now(int(user_to_unblock.get()), users, row_no))
                b2.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")
            else:
                Label(ub_frame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, relief="groove"). \
                    grid(row=2, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(ub_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: unblock.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(ub_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def post(self, post_id):
        personal_page = Toplevel()
        personal_page.title("Make Post")
        personal_page.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        pp_frame = LabelFrame(personal_page, text="Make a Post", font=("Roboto", 15), fg="#1877F2", padx=50,
                              pady=30)
        pp_frame.pack(padx=20, pady=20)

        Label(pp_frame, text="Post From", font=("Roboto", 15), padx=7, relief="groove"). \
            grid(row=0, column=0, columnspan=2, padx=4, pady=7, sticky="W")

        forum = StringVar()
        forum.set("Personal")
        Radiobutton(pp_frame, text="Personal", variable=forum, font=("Helvetica 18 bold", 12),
                    value="1", fg="#1877F2").grid(row=1, column=0, pady=7, sticky="W")
        Radiobutton(pp_frame, text="Page", variable=forum, font=("Helvetica 18 bold", 12),
                    value="0", fg="#1877F2").grid(row=1, column=1, pady=7, sticky="W")

        def post_in_page(page_ID, thepages, row_no):
            rp = csv.reader(open("Posts.csv"))
            linesp = list(rp)
            for lst in range(len(linesp)):
                if linesp[lst][3] == str(post_id):
                    linesp[lst][12] = thepages[int(page_ID) - 1]
                    break
            writer = csv.writer(open("Posts.csv", "w", newline=""))
            writer.writerows(linesp)

            Label(pp_frame, text="Posted.", font=("Roboto", 13), padx=20, pady=5). \
                grid(row=row_no + 3, column=0, columnspan=3, pady=7, sticky="W")
            # Back.
            Button(pp_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                   command=lambda: personal_page.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")

        def chosen(choice):
            if choice == str(1):
                Label(pp_frame, text="Posted from account.", font=("Roboto", 15), padx=7, relief="groove"). \
                    grid(row=3, column=0, columnspan=2, padx=4, pady=7, sticky="W")
                # Back.
                Button(pp_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: personal_page.destroy()).grid(row=4, column=0, pady=3, sticky="W")

            elif choice == str(0):

                pages_you_are_in = []
                with open("Page_Members.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[1] == str(self.ID):
                            pages_you_are_in.append(row[0])

                row_no = 2
                your_pages = []
                with open("Pages.csv.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(self.ID) or row[3] in pages_you_are_in:
                            your_pages.append(row[3])
                            Label(pp_frame, text=f"{row[4]}\nCreated by {row[1]} {row[2]} on {row[7]}\nCategory: "
                                                f"{row[5]}", font=("Roboto", 13), padx=20, pady=5, bd=1,
                                  relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                            row_no += 1

                if your_pages:
                    Label(pp_frame, text="Number of page\nyou want to post in: ", font=("Roboto", 13), padx=20, pady=5,
                          bd=1, relief="sunken", fg="#1877F2").grid(row=row_no + 1, column=0, columnspan=2, pady=10,
                                                                    padx=3, sticky="W")

                    selected_page = Entry(pp_frame, highlightthickness=2)
                    selected_page.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                    selected_page.grid(row=row_no + 1, column=2, sticky="E")

                    b2 = Button(pp_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                                command=lambda: post_in_page(selected_page.get(), your_pages, row_no))
                    b2.grid(row=row_no + 2, column=0, columnspan=3, pady=7, sticky="W")
                else:
                    Label(pp_frame, text="You've no page.\nPosted from account.", font=("Roboto", 13), padx=20, pady=5)\
                        .grid(row=row_no + 3, column=0, columnspan=3, pady=7, sticky="W")
                    # Back.
                    Button(pp_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: personal_page.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")

        Button(pp_frame, text="Enter", font=("Roboto", 12), width=7, fg="#1877F2", command=lambda: chosen(forum.get()))\
            .grid(row=2, column=0, columnspan=3, pady=(7, 0), sticky="W")

    def create_a_post(self):

        posting = Toplevel()
        posting.title("Creating Post")
        posting.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        po_frame = LabelFrame(posting, text="Create a New Post", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        po_frame.pack(padx=20, pady=20)

        Label(po_frame, text="Post Type", font=("Roboto", 15), padx=7). \
            grid(row=0, column=0, columnspan=2, padx=4, pady=(7, 0), sticky="W")
        Label(po_frame, text="Post Title", font=("Roboto", 15), padx=7). \
            grid(row=2, column=0, columnspan=2, padx=4, pady=7, sticky="W")
        Label(po_frame, text="Post Description", font=("Roboto", 15), padx=7). \
            grid(row=3, column=0, columnspan=2, padx=4, pady=7, sticky="W")
        Label(po_frame, text="File Path", font=("Roboto", 15), padx=7). \
            grid(row=5, column=0, columnspan=2, padx=4, pady=7, sticky="W")

        title = Entry(po_frame, highlightthickness=2)
        title.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        description = Entry(po_frame, highlightthickness=2)
        description.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        path = Entry(po_frame, highlightthickness=2)
        path.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

        ptype = StringVar()
        ptype.set("Image")
        Radiobutton(po_frame, text="Image", variable=ptype, font=("Helvetica 18 bold", 12),
                    value="Image", fg="#1877F2").grid(row=1, column=0, pady=7, sticky="W")
        Radiobutton(po_frame, text="Video", variable=ptype, font=("Helvetica 18 bold", 12),
                    value="Video", fg="#1877F2").grid(row=1, column=1, pady=7, sticky="W")

        title.grid(row=2, column=2, pady=7, sticky="E")
        description.grid(row=3, column=2, pady=7, sticky="E")
        path.grid(row=5, column=2, pady=7, sticky="E")

        def upload_file():
            po_frame.filename = filedialog.askopenfilename(
                initialdir=r"C:\Users\FUTURE LAPTOP\PycharmProjects\Facebook\Images", title="Select a File",
                filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
            path.insert(0, po_frame.filename)

        Button(po_frame, text="Upload", font=("Roboto", 12), width=7, fg="#1877F2", command=upload_file). \
            grid(row=4, column=0, columnspan=3, pady=(7,0), sticky="W")

        l2 = Label(po_frame, text="*Required field(s)\nempty.", font=("Helvetica 18 bold", 13),
                   padx=20, pady=4, bd=1, relief="groove", fg="#FF0000")

        def create_now():
            global l2_info

            if title.index("end") == 0 or description.index("end") == 0 or path.index("end") == 0:
                l2.grid(row=7, column=0, columnspan=2, pady=5, padx=3, sticky="W")
                l2_info = l2.grid_info()
            else:
                if l2_info != {}:
                    if l2_info["row"] == 7:
                        l2.destroy()

                post_obj = Post()

                post_obj.post_type = ptype.get()
                post_obj.post_title = title.get()
                post_obj.post_description = description.get()
                post_obj.file_path = path.get()
                post_obj.post_time = datetime.datetime.now().time().replace(microsecond=0)
                post_obj.post_date = datetime.datetime.now().date()

                # Each post gets a unique post id.
                r = csv.reader(open("Posts.csv"))
                lines = list(r)
                for lst in range(1, len(lines)):
                    if lines[lst][3]:
                        Post.post_id = lines[lst][3]

                post_obj.post_id = int(Post.post_id) + 1

                with open("Friends.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(self.ID) or row[3] == str(self.ID):
                            post_obj.post_recipients += 1

                # Adding user's post to database.
                with open("Posts.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow([self.ID, self.first_name, self.last_name, post_obj.post_id, post_obj.post_type,
                                         post_obj.post_title, post_obj.post_description, post_obj.post_time,
                                         post_obj.post_date, post_obj.privacy_id, post_obj.post_notification,
                                         post_obj.post_recipients, post_obj.page_id, post_obj.file_path])
                self.post(post_obj.post_id)

        Button(po_frame, text="Done", font=("Roboto", 14), width=9, bg="#1877F2", fg="white", command=create_now). \
            grid(row=6, column=0, columnspan=3, pady=7, sticky="W")

    def add_friend(self):
        adding = Toplevel()
        adding.title("Add Friend")
        adding.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        af_frame = LabelFrame(adding, text="Message a User", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        af_frame.pack(padx=15, pady=15)

        Label(af_frame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(af_frame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def send_request(user_ID, users, row_no):

            friend_ID = users[int(user_ID)-1]

            already_friends = False
            with open("Friends.csv") as friend_file:
                csv_reader = csv.reader(friend_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(self.ID) and row[3] == friend_ID and row[6] == str(False) or row[0] == friend_ID \
                            and row[3] == str(self.ID) and row[6] == str(False):
                        already_friends = True
                        break

            if not already_friends:

                request_pending = False
                with open("Friends.csv") as friend_file:
                    csv_reader = csv.reader(friend_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(self.ID) and row[3] == friend_ID and row[6] == str(True):
                            request_pending = True
                            break

                if request_pending:
                    Label(af_frame, text="Friend request pending.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                          relief="groove").grid(row=row_no + 3, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                    # Back.
                    Button(af_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: adding.destroy()).grid(row=row_no + 4, column=0, pady=3, sticky="W")
                else:
                    user_friend = Friend()
                    with open("Friends.csv", "a", newline="") as data_file:
                        csv_writer = csv.writer(data_file, delimiter=",")
                        csv_writer.writerow([self.ID, self.first_name, self.last_name, friend_ID,
                                             user_friend.first_name, user_friend.last_name, user_friend.pending])

                    Label(af_frame, text="Friend request sent.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                          relief="groove").grid(row=row_no + 3, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                    # Back.
                    Button(af_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                           command=lambda: adding.destroy()).grid(row=row_no+4, column=0, pady=3, sticky="W")
            else:
                Label(af_frame, text="You're already friends.", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="groove").grid(row=row_no + 3, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                # Back.
                Button(af_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: adding.destroy()).grid(row=row_no+4, column=0, pady=3, sticky="W")

        def info_entered(user_name):
            users = self.find_users(user_name)

            if users:
                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(af_frame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20,
                                  pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10,
                                                                      padx=3, sticky="W")
                            row_no += 1

                Label(af_frame, text="Number of profile\nyou want to befriend: ", font=("Roboto", 13), padx=20, pady=5,
                      bd=1, relief="sunken", fg="#1877F2").grid(row=row_no + 1, column=0, columnspan=2, pady=10, padx=3,
                                                                sticky="W")

                user_to_friend = Entry(af_frame, highlightthickness=2)
                user_to_friend.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_friend.grid(row=row_no + 1, column=2, sticky="E")

                b2 = Button(af_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: send_request(int(user_to_friend.get()), users, row_no))
                b2.grid(row=row_no + 2, column=0, columnspan=3, pady=7, sticky="W")
            else:
                Label(af_frame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, relief="groove"). \
                    grid(row=2, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(af_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: adding.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(af_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def send_message(self):
        messaging = Toplevel()
        messaging.title("Send Message")
        messaging.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        sm_frame = LabelFrame(messaging, text="Message a User", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        sm_frame.pack(padx=15, pady=15)

        Label(sm_frame, text="First Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        first_name = Entry(sm_frame, highlightthickness=2)
        first_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        first_name.grid(row=0, column=2, sticky="E")

        def send_now(ID, users, row_no, message_to_send):
            Label(sm_frame, text="Message sent.", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="groove"). \
                grid(row=row_no + 6, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            message_input = message_to_send
            user_ID = users[int(ID)-1]

            # Creating message object.
            message = Message()
            # Setting attributes.
            message.receiver_ID, message.sender_ID = user_ID, self.ID
            message.sender_first_name, message.sender_last_name = self.first_name, self.last_name
            message.content = message_input
            # Storing message data into a csv file.
            with open("Message.csv", "a", newline="") as data_file:
                csv_writer = csv.writer(data_file, delimiter=",")
                csv_writer.writerow([message.receiver_ID, message.sender_ID, message.sender_first_name,
                                     message.sender_last_name, message.content, message.pending])

        def type_message(user_ID, users, row_no):
            Label(sm_frame, text="Enter Message", font=("Roboto", 13), padx=15, pady=5, bd=1, relief="sunken"). \
                grid(row=row_no+3, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            message_content = Entry(sm_frame, highlightthickness=2)
            message_content.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
            message_content.grid(row=row_no+3, column=2, sticky="E")

            b3 = Button(sm_frame, text="Send", font=("Roboto", 13), width=7, fg="#1877F2",
                        command=lambda: send_now(user_ID, users, row_no, message_content.get()))
            b3.grid(row=row_no+5, column=0, columnspan=3, pady=7, sticky="W")

        def info_entered(user_name):
            users = self.find_users(user_name)

            if users:
                row_no = 2

                with open("Users_Database.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] in users:
                            Label(sm_frame, text=f"{row[1]} {row[2]}\nAbout: {row[7]}", font=("Roboto", 13), padx=20,
                                  pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2, pady=10,
                                                                      padx=3, sticky="W")
                            row_no += 1

                Label(sm_frame, text="Number of profile\nyou want to message: ", font=("Roboto", 13), padx=20, pady=5,
                      bd=1, relief="sunken", fg="#1877F2").grid(row=row_no + 1, column=0, columnspan=2, pady=10,
                                                                padx=3, sticky="W")

                user_to_message = Entry(sm_frame, highlightthickness=2)
                user_to_message.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                user_to_message.grid(row=row_no + 1, column=2, sticky="E")

                b2 = Button(sm_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: type_message(int(user_to_message.get()), users, row_no))
                b2.grid(row=row_no + 2, column=0, columnspan=3, pady=7, sticky="W")
            else:
                Label(sm_frame, text="User not found.", font=("Roboto", 13), padx=20, pady=5, relief="groove"). \
                    grid(row=2, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(sm_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: messaging.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(sm_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(first_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def create_a_page(self):

        paging = Toplevel()
        paging.title("Creating Page")
        paging.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        pg_frame = LabelFrame(paging, text="Create a New Page", font=("Roboto", 15), fg="#1877F2", padx=50, pady=30)
        pg_frame.pack(padx=20, pady=20)

        Label(pg_frame, text="Page Name", font=("Roboto", 15), padx=7). \
            grid(row=0, column=0, columnspan=2, padx=4, pady=(7, 0), sticky="W")
        Label(pg_frame, text="Page Category", font=("Roboto", 15), padx=7). \
            grid(row=2, column=0, columnspan=2, padx=4, pady=7, sticky="W")
        Label(pg_frame, text="Page Description", font=("Roboto", 15), padx=7). \
            grid(row=7, column=0, columnspan=2, padx=4, pady=7, sticky="W")

        pgname = Entry(pg_frame, highlightthickness=2)
        pgname.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        pgdescription = Entry(pg_frame, highlightthickness=2)
        pgdescription.config(highlightbackground="#1877F2", highlightcolor="#1877F2")

        pgcat = StringVar()
        pgcat.set("Local Business or Place")
        Radiobutton(pg_frame, text="Local Business or Place", variable=pgcat, font=("Helvetica 18 bold", 12),
                    value="Local Business or Place", fg="#1877F2").grid(row=3, column=0, pady=4, sticky="W")
        Radiobutton(pg_frame, text="Brand or Product", variable=pgcat, font=("Helvetica 18 bold", 12),
                    value="Brand or Product", fg="#1877F2").grid(row=4, column=0, pady=4, sticky="W")
        Radiobutton(pg_frame, text="Artist or Public Figure", variable=pgcat, font=("Helvetica 18 bold", 12),
                    value="Artist or Public Figure", fg="#1877F2").grid(row=5, column=0, pady=4, sticky="W")
        Radiobutton(pg_frame, text="Entertainment", variable=pgcat, font=("Helvetica 18 bold", 12),
                    value="Entertainment", fg="#1877F2").grid(row=6, column=0, pady=4, sticky="W")

        pgname.grid(row=0, column=2, pady=7, sticky="E")
        pgdescription.grid(row=7, column=2, pady=7, sticky="E")

        l3 = Label(pg_frame, text="*Required field(s)\nempty.", font=("Helvetica 18 bold", 13),
                   padx=20, pady=4, bd=1, relief="groove", fg="#FF0000")

        def create_now():
            global l3_info

            if pgname.index("end") == 0 or pgdescription.index("end") == 0:
                l3.grid(row=9, column=0, columnspan=2, pady=5, padx=3, sticky="W")
                l3_info = l3.grid_info()
            else:
                if l3_info != {}:
                    if l3_info["row"] == 9:
                        l3.destroy()

                page_obj = Page()

                page_obj.name = pgname.get()
                page_obj.category = pgcat.get()
                page_obj.description = pgdescription.get()
                page_obj.creation_date = datetime.datetime.now().date()

                # Each page gets a unique page id.
                r = csv.reader(open("Pages.csv.csv"))
                lines = list(r)
                for lst in range(1, len(lines)):
                    if lines[lst][3]:
                        Page.page_id = lines[lst][3]

                page_obj.page_id = int(Page.page_id) + 1

                # Adding user's page to database.
                with open("Pages.csv.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow([self.ID, self.first_name, self.last_name, page_obj.page_id, page_obj.name,
                                         page_obj.category, page_obj.description, page_obj.creation_date])
                # Page Created.
                Label(pg_frame, text="Page Created.", font=("Helvetica 18 bold", 14), padx=18, pady=4, bd=1,
                      relief="groove").grid(row=9, column=0, columnspan=3, pady=7, sticky="W")
                # Back.
                Button(pg_frame, text="Back", font=("Roboto", 14), width=9, fg="#1877F2",
                       command=lambda: paging.destroy()).grid(row=10, column=0, columnspan=3, pady=7, sticky="W")

        Button(pg_frame, text="Done", font=("Roboto", 14), width=9, bg="#1877F2", fg="white", command=create_now). \
            grid(row=8, column=0, columnspan=3, pady=7, sticky="W")

    @staticmethod
    def find_pages(name):
        pages = []
        with open("Pages.csv.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[4] == name:
                    pages.append(row[3])
        return pages

    def display_page(self, page_id):

        displaying_page = Toplevel()
        displaying_page.title("See Page")
        displaying_page.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        dpi_frame = LabelFrame(displaying_page, text="Page Info", font=("Roboto", 15), fg="#1877F2", padx=20,
                               pady=10)
        dpi_frame.grid(row=0, column=0, padx=20, pady=(15, 4), sticky="W")

        lp_frame = LabelFrame(displaying_page, text="Like Page", font=("Roboto", 15), fg="#1877F2", padx=20,
                              pady=10)
        lp_frame.grid(row=1, column=1, padx=20, pady=(15, 4), sticky="W")

        dpp_frame = LabelFrame(displaying_page, text="Page Posts", font=("Roboto", 15), fg="#1877F2", padx=20,
                               pady=10)
        dpp_frame.grid(row=1, column=0, padx=10, pady=(4, 15), sticky="W")

        def like_page_now(page_to_like_ID):

            global lpb

            already_liked = False
            with open("Page_Members.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == page_to_like_ID and row[1] == str(self.ID):
                        already_liked = True
                        break

            owner = False
            with open("Pages.csv.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(self.ID) and row[3] == page_to_like_ID:
                        owner = True
                        break

            if owner:
                lpb = Button(lp_frame, text="Like Page", width=12, font=("Roboto", 14), relief="raised",
                             state="disabled")
                Label(lp_frame, text="You created page.", font=("Roboto", 14), relief="groove"). \
                    grid(row=1, column=0, pady=3, sticky="W")
            elif not already_liked:
                with open("Page_Members.csv", "a", newline="") as data_file:
                    csv_writer = csv.writer(data_file, delimiter=",")
                    csv_writer.writerow([page_to_like_ID, self.ID])
                lpb = Button(lp_frame, text="Like Page", width=12, font=("Roboto", 14), relief="raised",
                             state="disabled")
                Label(lp_frame, text="Page Liked.", font=("Roboto", 14), relief="groove").\
                    grid(row=1, column=0, pady=3, sticky="W")
            else:
                lpb = Button(lp_frame, text="Like Page", width=12, font=("Roboto", 14), relief="raised",
                             state="disabled")
                Label(lp_frame, text="Page already liked.", font=("Roboto", 14), relief="groove").\
                    grid(row=1, column=0, pady=3, sticky="W")

        lpb = Button(lp_frame, text="Like Page", width=12, font=("Roboto", 14), relief="raised",
                     command=lambda: like_page_now(page_id))
        lpb.grid(row=0, column=0, sticky="W")

        with open("Pages.csv.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[3] == page_id:
                    name = row[4]
                    creator_first = row[1]
                    creator_last = row[2]
                    category = row[5]
                    page_des = row[6]
                    created_date = row[7]

        Label(dpi_frame, text="Name:", font=("Roboto", 13)).grid(row=1, column=0, pady=3, sticky="W")
        Label(dpi_frame, text=name, font=("Helvetica", 13)).grid(row=1, column=1, pady=3, sticky="W")
        Label(dpi_frame, text="Created By: ", font=("Roboto", 13)).grid(row=2, column=0, pady=3, sticky="W")
        Label(dpi_frame, text=creator_first + "" + creator_last, font=("Helvetica", 13)).grid(row=2, column=1, pady=3,
                                                                                              sticky="W")
        Label(dpi_frame, text="Created On: ", font=("Roboto", 13)).grid(row=3, column=0, pady=3, sticky="W")
        Label(dpi_frame, text=created_date, font=("Helvetica", 13)).grid(row=3, column=1, pady=3, sticky="W")
        Label(dpi_frame, text="Category: ", font=("Roboto", 13)).grid(row=4, column=0, pady=3, sticky="W")
        Label(dpi_frame, text=category, font=("Helvetica", 13)).grid(row=4, column=1, pady=3, sticky="W")
        Label(dpi_frame, text="Description: ", font=("Roboto", 13)).grid(row=5, column=0, pady=3, sticky="W")
        Label(dpi_frame, text=page_des, font=("Helvetica", 13)).grid(row=5, column=1, pady=3, sticky="W")

        pstitle1 = []
        psdescription1 = []
        ps_postid = []
        ps_userid = []
        psfirst = []
        pslast = []
        global psfilepath1
        global psImage1
        global images1
        global title_label1
        global image_label1
        global description_label1
        global button_forward1
        global button_back1
        global button_comment
        global name_label
        images1.clear()
        psfilepath1.clear()
        post_num = 1

        has_posts = False
        with open("Posts.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[12] == page_id:
                    psfirst.append(row[1])
                    pslast.append(row[2])
                    ps_userid.append(row[0])
                    ps_postid.append(row[3])
                    pstitle1.append(row[5])
                    psdescription1.append(row[6])
                    psfilepath1.append(row[13])
                    has_posts = True

        if has_posts:
            for pic in psfilepath1:
                my_pic = Image.open(pic)
                resized = my_pic.resize((320, 220))
                new_pic = ImageTk.PhotoImage(resized)
                images1.append(new_pic)

            title_label1 = Label(dpp_frame, text=pstitle1[post_num - 1], font=("Roboto", 13), padx=7,
                                 pady=5)
            image_label1 = Label(dpp_frame, image=images1[post_num - 1])
            description_label1 = Label(dpp_frame, text=psdescription1[post_num - 1],
                                       font=("Helvetica bold 18", 13), padx=7, pady=3)
            name_label = Label(dpp_frame, text="Posted by " + psfirst[post_num - 1] + " " + pslast[post_num-1],
                               font=("Roboto", 13), padx=7, pady=3)

            def forward(p_num):
                global title_label1
                global image_label1
                global description_label1
                global button_forward1
                global button_back1
                global button_comment
                global name_label
                global images1

                title_label1.grid_forget()
                image_label1.grid_forget()
                description_label2.grid_forget()

                title_label1 = Label(dpp_frame, text=pstitle1[p_num - 1], font=("Roboto", 13), padx=7,
                                     pady=5)
                image_label1 = Label(dpp_frame, image=images1[p_num - 1])
                description_label1 = Label(dpp_frame, text=psdescription1[p_num - 1],
                                           font=("Helvetica bold 18", 13), padx=7, pady=3)
                name_label = Label(dpp_frame, text="Posted by " + psfirst[p_num - 1] + " " + pslast[p_num - 1],
                                   font=("Roboto", 13), padx=7, pady=3)

                button_forward1 = Button(dpp_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                         command=lambda: forward(p_num + 1))
                button_back1 = Button(dpp_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                      command=lambda: back(p_num - 1))
                button_comment = Button(dpp_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                        command=lambda: Post.comment_on_a_post(ps_postid[p_num - 1],
                                                                               ps_userid[p_num - 1], self))

                if p_num == len(images1):
                    button_forward1 = Button(dpp_frame, text=">>", width=6, font=("Roboto", 13),
                                             state="disabled")

                title_label1.grid(row=0, column=0, sticky="W")
                image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                description_label1.grid(row=2, column=0, sticky="W", pady=7)
                button_forward1.place(x=250, y=300)
                button_comment.place(x=100, y=300)
                button_back1.grid(row=3, column=0, sticky="W")
                name_label.grid(row=4, column=0, sticky="W")

            def back(p_num):
                global title_label1
                global image_label1
                global description_label1
                global button_forward1
                global button_back1
                global name_label
                global button_comment
                global images1

                title_label1.grid_forget()
                image_label1.grid_forget()
                description_label1.grid_forget()

                title_label1 = Label(dpp_frame, text=pstitle1[p_num - 1], font=("Roboto", 13), padx=7,
                                     pady=5)
                image_label1 = Label(dpp_frame, image=images1[p_num - 1])
                description_label1 = Label(dpp_frame, text=psdescription1[p_num - 1],
                                           font=("Helvetica bold 18", 13), padx=7, pady=3)
                name_label = Label(dpp_frame, text="Posted by " + psfirst[p_num - 1] + " " + pslast[p_num - 1],
                                   font=("Roboto", 13), padx=7, pady=3)

                button_forward1 = Button(dpp_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                         command=lambda: forward(p_num + 1))
                button_back1 = Button(dpp_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                      command=lambda: back(p_num - 1))
                button_comment = Button(dpp_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                        command=lambda: Post.comment_on_a_post(ps_postid[p_num - 1], ps_userid[p_num - 1],
                                                                               self))

                if p_num == 1:
                    button_back1 = Button(dpp_frame, text="<<", width=6, font=("Roboto", 13),
                                          state="disabled")

                title_label1.grid(row=0, column=0, sticky="W")
                image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
                description_label1.grid(row=2, column=0, sticky="W", pady=7)
                button_forward1.place(x=250, y=300)
                button_comment.place(x=100, y=300)
                button_back1.grid(row=3, column=0, sticky="W")
                name_label.grid(row=4, column=0, sticky="W")

            if len(images1) != 1:
                button_forward1 = Button(dpp_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                         command=lambda: forward(post_num + 1))
                button_back1 = Button(dpp_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                      command=lambda: back(post_num))
            else:
                button_forward1 = Button(dpp_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                         state="disabled")
                button_back1 = Button(dpp_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2", state="disabled")

            button_comment = Button(dpp_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                    command=lambda: Post.comment_on_a_post(ps_postid[post_num - 1],
                                                                           ps_userid[post_num - 1], self))

            title_label1.grid(row=0, column=0, sticky="W")
            image_label1.grid(row=1, column=0, columnspan=2, sticky="W")
            description_label1.grid(row=2, column=0, sticky="W", pady=7)
            button_forward1.place(x=250, y=300)
            button_comment.place(x=100, y=300)
            button_back1.grid(row=3, column=0, sticky="W")
            name_label.grid(row=4, column=0, sticky="W")

        if not has_posts:
            Label(dpp_frame, text="Page has no posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3, sticky="W")

    def search_page(self):
        search_page_win = Toplevel()
        search_page_win.title("Search Page")
        search_page_win.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        sp_frame = LabelFrame(search_page_win, text="Search a Page", font=("Roboto", 15), fg="#1877F2", padx=50,
                              pady=30)
        sp_frame.pack(padx=20, pady=20)

        Label(sp_frame, text="Page Name", font=("Roboto", 13), padx=20, pady=5, bd=1, relief="sunken"). \
            grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        page_name = Entry(sp_frame, highlightthickness=2)
        page_name.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
        page_name.grid(row=0, column=2, sticky="E")

        def search_now(ID, pages_found):
            page_ID = pages_found[ID - 1]
            # Destroying the search window and displaying the page.
            search_page_win.destroy()
            self.display_page(page_ID)

        def info_entered(name):
            pages_to_find = self.find_pages(name)

            if pages_to_find:
                row_no = 2

                with open("Pages.csv.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[4] == name:
                            Label(sp_frame, text=f"{row[4]}\nCreated By: {row[1]} {row[2]}", font=("Roboto", 13),
                                  padx=20, pady=5, bd=1, relief="groove").grid(row=row_no, column=0, columnspan=2,
                                                                               pady=10, padx=3, sticky="W")
                            row_no += 1

                Label(sp_frame, text="Number of page\nyou want to see: ", font=("Roboto", 13), padx=20, pady=5, bd=1,
                      relief="sunken", fg="#1877F2").grid(row=row_no + 1, column=0, columnspan=2, pady=10, padx=3,
                                                          sticky="W")

                page_to_see = Entry(sp_frame, highlightthickness=2)
                page_to_see.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
                page_to_see.grid(row=row_no + 1, column=2, sticky="E")

                b2 = Button(sp_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                            command=lambda: search_now(int(page_to_see.get()), pages_to_find))
                b2.grid(row=row_no + 2, column=0, columnspan=3, pady=7, sticky="W")
            else:
                Label(sp_frame, text="Page not found.", font=("Roboto", 14), padx=20, pady=5, bd=1, relief="sunken"). \
                    grid(row=2, column=0, columnspan=2, pady=10, padx=3, sticky="W")
                # Back.
                Button(sp_frame, text="Back", width=7, font=("Roboto", 13), fg="#1877F2",
                       command=lambda: search_page_win.destroy()).grid(row=3, column=0, pady=3, sticky="W")

        b1 = Button(sp_frame, text="Enter", font=("Roboto", 13), width=7, fg="#1877F2",
                    command=lambda: info_entered(page_name.get()))
        b1.grid(row=1, column=0, columnspan=3, pady=7, sticky="W")

    def like_a_page(self, page_id):
        pass

    def display_user_profile(self, ID):
        displaying = Toplevel()
        displaying.title("See User")
        displaying.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        pi_frame = LabelFrame(displaying, text="Profile Info.", font=("Roboto", 15), fg="#1877F2", padx=40, pady=20)
        pi_frame.grid(row=0, column=0, sticky="W", padx=15, pady=(10, 5))

        up_frame = LabelFrame(displaying, text="Posts", font=("Roboto", 15), fg="#1877F2", padx=40, pady=20)
        up_frame.grid(row=1, column=0, sticky="W", padx=15, pady=(5, 10))

        pstitle2 = []
        psdescription2 = []
        ps_postid = []
        global psfilepath2
        global psImage2
        global images2
        global title_label2
        global image_label2
        global description_label2
        global button_forward2
        global button_back2
        global button_comment
        images2.clear()
        psfilepath2.clear()

        private_account = False
        with open("Users_Database.csv") as data_file:
            csv_reader = csv.reader(data_file, delimiter=",")
            for row in csv_reader:
                if row[0] == ID:
                    Label(pi_frame, text=f"{row[1]} {row[2]}", font=("Roboto", 12)).\
                        grid(row=0, column=0, pady=3, sticky="W")
                    about = row[7]
                    current_city = row[8]
                    education = row[9]
                    workplace = row[10]
                    status = row[11]
                if row[0] == ID and row[12] == str(True):
                    private_account = True

        Label(pi_frame, text="About:", font=("Roboto", 12)).grid(row=1, column=0, pady=3, sticky="W")
        Label(pi_frame, text=about, font=("Helvetica", 12)).grid(row=1, column=1, pady=3, sticky="W")
        Label(pi_frame, text="Current City: ", font=("Roboto", 12)).grid(row=2, column=0, pady=3, sticky="W")
        Label(pi_frame, text=current_city, font=("Helvetica", 12)).grid(row=2, column=1, pady=3, sticky="W")
        Label(pi_frame, text="education: ", font=("Roboto", 12)).grid(row=3, column=0, pady=3, sticky="W")
        Label(pi_frame, text=education, font=("Helvetica", 12)).grid(row=3, column=1, pady=3, sticky="W")
        Label(pi_frame, text="workplace: ", font=("Roboto", 12)).grid(row=4, column=0, pady=3, sticky="W")
        Label(pi_frame, text=workplace, font=("Helvetica", 12)).grid(row=4, column=1, pady=3, sticky="W")
        Label(pi_frame, text="Relationship status: ", font=("Roboto", 12)).grid(row=5, column=0, pady=3, sticky="W")
        Label(pi_frame, text=status, font=("Helvetica", 12)).grid(row=5, column=1, pady=3, sticky="W")

        # If that user's account is public.
        if not private_account:
            # Display Posts.
            post_num = 1

            has_posts = False
            with open("Posts.csv") as data_file:
                csv_reader = csv.reader(data_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(ID) and row[9] == str(0) and not row[12]:
                        ps_postid.append(row[3])
                        pstitle2.append(row[5])
                        psdescription2.append(row[6])
                        psfilepath2.append(row[13])
                        has_posts = True
            if has_posts:
                for pic in psfilepath2:
                    my_pic = Image.open(pic)
                    resized = my_pic.resize((320, 220))
                    new_pic = ImageTk.PhotoImage(resized)
                    images2.append(new_pic)

                title_label2 = Label(up_frame, text=pstitle2[post_num - 1], font=("Roboto", 13), padx=7,
                                     pady=5)
                image_label2 = Label(up_frame, image=images2[post_num - 1])
                description_label2 = Label(up_frame, text=psdescription2[post_num - 1],
                                           font=("Helvetica bold 18", 13), padx=7, pady=3)

                def forward(p_num):
                    global title_label2
                    global image_label2
                    global description_label2
                    global button_forward2
                    global button_back2
                    global button_comment
                    global images2

                    title_label2.grid_forget()
                    image_label2.grid_forget()
                    description_label2.grid_forget()

                    title_label2 = Label(up_frame, text=pstitle2[p_num - 1], font=("Roboto", 13), padx=7,
                                         pady=5)
                    image_label2 = Label(up_frame, image=images2[p_num - 1])
                    description_label2 = Label(up_frame, text=psdescription2[p_num - 1],
                                               font=("Helvetica bold 18", 13), padx=7, pady=3)

                    button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                             command=lambda: forward(p_num + 1))
                    button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                          command=lambda: back(p_num - 1))
                    if pstitle2[p_num-1] == "None":
                        button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                state="disabled")
                    else:
                        button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                command=lambda: Post.comment_on_a_post(ps_postid[p_num-1], ID, self))

                    if p_num == len(images1):
                        button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13),
                                                 state="disabled")

                    title_label2.grid(row=0, column=0, sticky="W")
                    image_label2.grid(row=1, column=0, columnspan=2, sticky="W")
                    description_label2.grid(row=2, column=0, sticky="W", pady=7)
                    button_forward2.place(x=250, y=300)
                    button_comment.place(x=100, y=300)
                    button_back2.grid(row=3, column=0, sticky="W")

                def back(p_num):
                    global title_label2
                    global image_label2
                    global description_label2
                    global button_forward2
                    global button_back2
                    global button_comment
                    global images2

                    title_label2.grid_forget()
                    image_label2.grid_forget()
                    description_label2.grid_forget()

                    title_label2 = Label(up_frame, text=pstitle2[p_num - 1], font=("Roboto", 13), padx=7,
                                         pady=5)
                    image_label2 = Label(up_frame, image=images2[p_num - 1])
                    description_label2 = Label(up_frame, text=psdescription2[p_num - 1],
                                               font=("Helvetica bold 18", 13), padx=7, pady=3)

                    button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                             command=lambda: forward(p_num + 1))
                    button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                          command=lambda: back(p_num - 1))
                    if pstitle2[p_num-1] == "None":
                        button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                state="disabled")
                    else:
                        button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                command=lambda: Post.comment_on_a_post(ps_postid[p_num-1], ID, self))

                    if p_num == 1:
                        button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13),
                                              state="disabled")

                    title_label2.grid(row=0, column=0, sticky="W")
                    image_label2.grid(row=1, column=0, columnspan=2, sticky="W")
                    description_label2.grid(row=2, column=0, sticky="W", pady=7)
                    button_forward2.place(x=250, y=300)
                    button_comment.place(x=100, y=300)
                    button_back2.grid(row=3, column=0, sticky="W")

                if len(images2) != 1:
                    button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                             command=lambda: forward(post_num + 1))
                    button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                          command=lambda: back(post_num))
                else:
                    button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                             state="disabled")
                    button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                          state="disabled")

                if pstitle2[post_num - 1] == "None":
                    button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                            state="disabled")
                else:
                    button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                            command=lambda: Post.comment_on_a_post(ps_postid[post_num - 1], ID, self))

                title_label2.grid(row=0, column=0, sticky="W")
                image_label2.grid(row=1, column=0, columnspan=2, sticky="W")
                description_label2.grid(row=2, column=0, sticky="W", pady=7)
                button_forward2.place(x=250, y=300)
                button_comment.place(x=100, y=300)
                button_back2.grid(row=3, column=0, sticky="W")

            if not has_posts:
                Label(up_frame, text="User has no posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3,
                                                                                     sticky="W")
        else:
            # Else checking if you are friends with that user.
            friends = False
            with open("Friends.csv") as friend_file:
                csv_reader = csv.reader(friend_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == str(self.ID) and row[3] == str(ID) or row[0] == str(ID) and row[3] == str(self.ID):
                        friends = True
                        break
            if friends:
                post_num = 1

                has_posts = False
                with open("Posts.csv") as data_file:
                    csv_reader = csv.reader(data_file, delimiter=",")
                    for row in csv_reader:
                        if row[0] == str(ID) and row[9] == str(0) and not row[12]:
                            ps_postid.append(row[3])
                            pstitle2.append(row[5])
                            psdescription2.append(row[6])
                            psfilepath2.append(row[13])
                            has_posts = True

                if has_posts:
                    for pic in psfilepath2:
                        my_pic = Image.open(pic)
                        resized = my_pic.resize((320, 220))
                        new_pic = ImageTk.PhotoImage(resized)
                        images2.append(new_pic)

                    title_label2 = Label(up_frame, text=pstitle2[post_num - 1], font=("Roboto", 13), padx=7,
                                         pady=5)
                    image_label2 = Label(up_frame, image=images2[post_num - 1])
                    description_label2 = Label(up_frame, text=psdescription2[post_num - 1],
                                               font=("Helvetica bold 18", 13), padx=7, pady=3)

                    def forward(p_num):
                        global title_label2
                        global image_label2
                        global description_label2
                        global button_forward2
                        global button_back2
                        global button_comment
                        global images2

                        title_label2.grid_forget()
                        image_label2.grid_forget()
                        description_label2.grid_forget()

                        title_label2 = Label(up_frame, text=pstitle2[p_num - 1], font=("Roboto", 13), padx=7,
                                             pady=5)
                        image_label2 = Label(up_frame, image=images2[p_num - 1])
                        description_label2 = Label(up_frame, text=psdescription2[p_num - 1],
                                                   font=("Helvetica bold 18", 13), padx=7, pady=3)

                        button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: forward(p_num + 1))
                        button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                              command=lambda: back(p_num - 1))
                        if pstitle2[p_num - 1] == "None":
                            button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13),
                                                    fg="#1877F2",
                                                    state="disabled")
                        else:
                            button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13),
                                                    fg="#1877F2",
                                                    command=lambda: Post.comment_on_a_post(ps_postid[p_num - 1], ID,
                                                                                           self))

                        if p_num == len(images2):
                            button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13),
                                                     state="disabled")

                        title_label2.grid(row=0, column=0, sticky="W")
                        image_label2.grid(row=1, column=0, columnspan=2, sticky="W")
                        description_label2.grid(row=2, column=0, sticky="W", pady=7)
                        button_forward2.place(x=250, y=300)
                        button_comment.place(x=100, y=300)
                        button_back2.grid(row=3, column=0, sticky="W")

                    def back(p_num):
                        global title_label2
                        global image_label2
                        global description_label2
                        global button_forward2
                        global button_back2
                        global button_comment
                        global images2

                        title_label2.grid_forget()
                        image_label2.grid_forget()
                        description_label2.grid_forget()

                        title_label2 = Label(up_frame, text=pstitle2[p_num - 1], font=("Roboto", 13), padx=7,
                                             pady=5)
                        image_label2 = Label(up_frame, image=images2[p_num - 1])
                        description_label2 = Label(up_frame, text=psdescription2[p_num - 1],
                                                   font=("Helvetica bold 18", 13), padx=7, pady=3)

                        button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: forward(p_num + 1))
                        button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                              command=lambda: back(p_num - 1))
                        if pstitle2[p_num - 1] == "None":
                            button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13),
                                                    fg="#1877F2",
                                                    state="disabled")
                        else:
                            button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13),
                                                    fg="#1877F2",
                                                    command=lambda: Post.comment_on_a_post(ps_postid[p_num - 1], ID,
                                                                                           self))

                        if p_num == 1:
                            button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13),
                                                  state="disabled")

                        title_label2.grid(row=0, column=0, sticky="W")
                        image_label2.grid(row=1, column=0, columnspan=2, sticky="W")
                        description_label2.grid(row=2, column=0, sticky="W", pady=7)
                        button_forward2.place(x=250, y=300)
                        button_comment.place(x=100, y=300)
                        button_back2.grid(row=3, column=0, sticky="W")

                    if len(images2) != 1:
                        button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 command=lambda: forward(post_num + 1))
                        button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                              command=lambda: back(post_num))
                    else:
                        button_forward2 = Button(up_frame, text=">>", width=6, font=("Roboto", 13), fg="#1877F2",
                                                 state="disabled")
                        button_back2 = Button(up_frame, text="<<", width=6, font=("Roboto", 13), fg="#1877F2",
                                              state="disabled")

                    if pstitle2[post_num - 1] == "None":
                        button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                state="disabled")
                    else:
                        button_comment = Button(up_frame, text="Comment", width=10, font=("Roboto", 13), fg="#1877F2",
                                                command=lambda: Post.comment_on_a_post(ps_postid[post_num - 1], ID,
                                                                                       self))

                    title_label2.grid(row=0, column=0, sticky="W")
                    image_label2.grid(row=1, column=0, columnspan=2, sticky="W")
                    description_label2.grid(row=2, column=0, sticky="W", pady=7)
                    button_forward2.place(x=250, y=300)
                    button_comment.place(x=100, y=300)
                    button_back2.grid(row=3, column=0, sticky="W")

                if not has_posts:
                    Label(up_frame, text="User has no posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3,
                                                                                         sticky="W")
            else:
                # You can't view user's post.
                Label(up_frame, text="You can't view posts.", font=("Roboto", 14)).grid(row=0, column=0, pady=3,
                                                                                        sticky="W")

    def accept_decline_friend_request(self):
        accept_decline = Toplevel()
        accept_decline.title("Friend Requests")
        accept_decline.iconbitmap(r"C:\Users\FUTURE LAPTOP\Downloads\fbicon.ico")

        ad_frame = LabelFrame(accept_decline, text="Friend Requests Pending", font=("Roboto", 15), fg="#1877F2",
                              padx=50, pady=30)
        ad_frame.pack(padx=15, pady=15)

        Label(ad_frame, text="New Friend Requests: ", font=("Roboto", 14), padx=5, pady=5, bd=1, relief="sunken",
              fg="#1877F2").grid(row=0, column=0, columnspan=2, pady=10, padx=3, sticky="W")

        global request_to_accept
        global request_to_reject
        global friend_request
        global acl
        global adl
        global ta
        global la
        global ta_info
        global la_info

        l5 = Label(ad_frame, text="*Required field(s)\nempty.", font=("Helvetica 18 bold", 13),
                   padx=20, pady=4, bd=1, relief="groove", fg="#FF0000")

        sender_first_name = []
        sender_last_name = []
        sender_id = []
        pending_friend_request = False
        with open("Friends.csv") as friend_file:
            csv_reader = csv.reader(friend_file, delimiter=",")
            for row in csv_reader:
                if row[3] == str(self.ID) and row[6] == str(True):
                    pending_friend_request = True
                    sender_first_name.append(row[1])
                    sender_last_name.append(row[2])
                    sender_id.append(row[0])
                    break

        def accept_request(friend_request_no, sen_ID, row_no):
            global request_to_accept
            global acl
            global request_to_reject
            global adl

            r = csv.reader(open("Friends.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][3] == str(self.ID) and lines[lst][6] == str(True) and lines[lst][0] == \
                        sen_ID[int(friend_request_no)-1]:
                    lines[lst][4], lines[lst][5], lines[lst][6] = self.first_name, self.last_name, False
            writer = csv.writer(open("Friends.csv", "w", newline=""))
            writer.writerows(lines)

            request_to_accept.grid_forget()
            acl.grid_forget()

            request_to_accept.grid_forget()
            acl.grid_forget()
            request_to_reject.grid_forget()
            adl.grid_forget()

            take_action(row_no)

        def decline_request(friend_request_no, sen_ID, row_no):
            global request_to_accept
            global acl
            global request_to_reject
            global adl

            r = csv.reader(open("Friends.csv"))
            lines = list(r)
            for lst in range(len(lines)):
                if lines[lst][3] == str(self.ID) and lines[lst][6] == str(True) and lines[lst][0] == \
                        sen_ID[int(friend_request_no) - 1]:
                    lines.remove(lines[lst])
                    break
            writer = csv.writer(open("Friends.csv", "w", newline=""))
            writer.writerows(lines)

            request_to_accept.grid_forget()
            acl.grid_forget()
            request_to_reject.grid_forget()
            adl.grid_forget()

            take_action(row_no)

        def take_action(row_no):
            global ta
            global la
            global acl
            global adl
            global request_to_accept
            global request_to_reject
            global ta_info
            global la_info
            if ta.grid_info() != {}:
                ta.grid_forget()
            if la.grid_info() != {}:
                la.grid_forget()
            acl = Label(ad_frame, text="Number of request\nyou want to accept: ", font=("Roboto", 13), padx=4, pady=5,
                        bd=1, relief="sunken")
            acl.grid(row=row_no + 1, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            request_to_accept = Entry(ad_frame, highlightthickness=2)
            request_to_accept.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
            request_to_accept.grid(row=row_no + 1, column=2, sticky="E")

            adl = Label(ad_frame, text="Number of request\nyou want to decline: ", font=("Roboto", 13), padx=4, pady=5,
                        bd=1, relief="sunken")
            adl.grid(row=row_no + 3, column=0, columnspan=2, pady=10, padx=3, sticky="W")

            request_to_reject = Entry(ad_frame, highlightthickness=2)
            request_to_reject.config(highlightbackground="#1877F2", highlightcolor="#1877F2")
            request_to_reject.grid(row=row_no + 3, column=2, sticky="E")

            acb = Button(ad_frame, text="Accept", font=("Roboto", 13), width=7, bg="#1877F2", fg="white",
                         command=lambda: accept_request(request_to_accept.get(), sender_id, row_no))
            acb.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")

            deb = Button(ad_frame, text="Decline", font=("Roboto", 13), width=10, bg="#1877F2", fg="white",
                         command=lambda: decline_request(request_to_reject.get(), sender_id, row_no))
            deb.grid(row=row_no+4, column=0, columnspan=3, pady=7, sticky="W")

            Button(ad_frame, text="Done", font=("Roboto", 13), width=10, command=lambda: accept_decline.destroy())\
                .grid(row=row_no + 5, column=0, columnspan=3, pady=7, sticky="W")

        if pending_friend_request:

            row_no = 1

            with open("Friends.csv") as friend_file:
                csv_reader = csv.reader(friend_file, delimiter=",")
                for row in csv_reader:
                    if row[3] == str(self.ID) and row[6] == str(True):
                        Label(ad_frame, text=f"You've a new friend request\nfrom {row[1]} {row[2]}.",
                              font=("Roboto", 13), padx=20, pady=5, bd=1, relief="groove").grid(row=row_no, column=0,
                                                                                                columnspan=2, pady=10,
                                                                                                padx=3, sticky="W")
                        row_no += 1

            ta = Button(ad_frame, text="Take Action", font=("Roboto", 13), width=12, bg="#1877F2", fg="white",
                        command=lambda: take_action(row_no))
            ta.grid(row=row_no+1, column=0, columnspan=3, pady=7, sticky="W")
            ta_info = ta.grid_info()
            la = Button(ad_frame, text="Later", font=("Roboto", 13), width=10, bg="#1877F2", fg="white",
                        command=lambda: accept_decline.destroy())
            la.grid(row=row_no+2, column=0, columnspan=3, pady=7, sticky="W")
            la_info = la.grid_info()

        else:
            Label(ad_frame, text="No new friend requests.", font=("Roboto", 13), padx=20, pady=4, bd=1, relief="groove").\
                grid(row=0, column=0, padx=4, pady=7, sticky="W")


def gui(obj):
    # Initial Frame.
    global myFrame
    myFrame = LabelFrame(root, padx=70, pady=70, text="Welcome to Facebook", font=("Roboto", 18), fg="#1877F2")
    myFrame.pack(padx=50, pady=25)

    # Login and Sign Up Buttons.
    global loginButton
    loginButton = Button(myFrame, text="Login", padx=35, pady=10, font=("Roboto", 14), command=obj.login)
    Label(myFrame, text="OR", font="Roboto", fg="#1877F2").grid(row=1, column=1, pady=10)
    global signButton
    signButton = Button(myFrame, text="Sign Up", padx=35, pady=10, font=("Roboto", 14),
                        command=obj.sign_up)

    loginButton.grid(row=0, column=1)
    signButton.grid(row=2, column=1)

    root.mainloop()


u1 = User()


gui(u1)