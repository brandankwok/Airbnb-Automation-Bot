from booking.booking import Booking

try:
    with Booking() as bot:
        bot.load_first_page()
        bot.search_location(input("Where do you want to go? "))
        bot.select_dates(input("What is the check in date (YYYY-MM-DD)? "), input("What is the check out date (YYYY-MM-DD)? "))
        adults = int(input("How many adults are going? "))
        children = int(input("How many children are going? "))
        bot.select_guests(adults, children)
        bot.click_search()
        bot.refresh()
        bot.apply_filters(int(input("What is your maximum price per night? $")), adults+children)
        bot.refresh()
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise