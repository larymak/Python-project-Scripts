from booking.booking import booking
import time 
bot=booking()
try:
    with bot:
        bot.land_first_page()
        print('exiting .......')
        bot.cross_check()
        bot.change_currency()
        bot.select_searchbar("New York")
        bot.enter_dates(checkin="2023-07-16",checkout="2023-07-21")
        bot.booking_count_inc(4,None,None)
        bot.click_search()
        bot.apply_filtration()
        bot.refresh()
        bot.report_results()

        # print(len(bot.report_results()))

except Exception as e:
    if 'in PATH' in e:
        print("there is a problem at CLI ", e )
        print("add path as ")
        print("windows  :  PATH=%PATH%;C:PATH-TO-YOUR-FOLDER")
    else:
        raise


time.sleep(100)
bot.quit()
