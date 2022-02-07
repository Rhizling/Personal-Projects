import tkinter as tk
import tkinter.font as font
from tkinter import Button

from Site import Site


def add_site(site: Site):
    # will add a site created by the user to the next empty slot in the grid
    sites.append(site)
    current_page = create_info_page(site)
    new_button = tk.Button(sites_page, text=site.name, relief="raised", width=10, height=2,
                           command=lambda: open_site_click(current_page))
    for row in range(NUM_OF_GRID_ROWS):
        for col in range(NUM_OF_GRID_COLS):
            for current_button in sites_frame.grid_slaves(row, col):
                if current_button.cget('text') == "":
                    new_button.grid(row=row, column=col, pady=2, padx=2)
                    break


def open_site_click(page: tk.Tk):
    # Opens a site page
    page.deiconify()


def create_info_page(site: Site):
    # Creates a page and returns it
    info_page = tk.Tk()
    info_page.title(site.name)
    info_page.geometry("100x100")
    info_page.withdraw()
    return info_page


def add_null_site(grid_row, grid_col):
    # adds the default type of site necessary for initializing the original grid
    button = tk.Button(sites_page, text="", relief="flat", width=10, height=2)
    button.grid(row=grid_row, column=grid_col, pady=2, padx=2)


NUM_OF_GRID_ROWS = 20
NUM_OF_GRID_COLS = 14


def create_sites_grid():
    # creates the default grid for all null site buttons - uses the add_null_site function

    for row in range(NUM_OF_GRID_ROWS):
        for col in range(NUM_OF_GRID_COLS):
            add_null_site(grid_row=row, grid_col=col)
    home_page_exit = tk.Button(sites_page, text="Back\nto\nMain", relief='ridge', width=7, height=50, bg='light blue',
                               command=sites_exit_button)
    home_page_exit.grid(rowspan=14, column=14, row=0)


def sites_exit_button():
    sites_page.withdraw()
    home_page.deiconify()


def view_sites_click():
    # allows functionality for the view_sites button on the home page
    home_page.withdraw()
    sites_page.deiconify()


def add_sites_click():
    # allows functionality for the add_sites button on the home page
    home_page.withdraw()
    add_site_page.deiconify()


def submit():
    # provides functionality for submit button in add sites page
    add_site_page.withdraw()
    home_page.deiconify()
    site_name = site_entry.get()
    site_username = username_entry.get()
    site_password = password_entry.get()
    new_site = Site(name=site_name, username=site_username, password=site_password)
    add_site(new_site)


# home page gui
home_page = tk.Tk()
home_page.configure(bg='light blue')
home_page.title("Personal Password Archive")
home_page.geometry("500x500")
title_name = tk.Label(home_page, text="Password Manager", bg='light grey', font=font.Font(family="Times", size=30))
title_name.place(x=130, y=45)
home_middle_frame = tk.Frame(home_page, bg='light grey', height=300, width=200)
home_middle_frame.place(x=150, y=130)
home_page.withdraw()
# home page buttons functionalities and placements
sites_button = tk.Button(home_middle_frame, text="View Sites", relief="raised", width=10, height=2,
                         command=view_sites_click)
sites_button.place(x=57, y=30)
add_sites_button = tk.Button(home_middle_frame, text="Add Sites", relief="raised", width=10, height=2,
                             command=add_sites_click)
add_sites_button.place(x=57, y=80)
set_password_button = tk.Button(home_middle_frame, text="Remove Sites", relief="raised", width=10, height=2)
set_password_button.place(x=57, y=130)
edit_password_button = tk.Button(home_middle_frame, text="Lock Status", relief="raised", width=10, height=2)
edit_password_button.place(x=57, y=180)
set_lock_button = tk.Button(home_middle_frame, text="Set Lock", relief="raised", width=10, height=2)
set_lock_button.place(x=57, y=230)
# sites page gui
sites_page = tk.Tk()
sites_page.configure(bg='light grey')
sites_page.title("Sites")
sites_page.geometry("1372x760")
sites_frame = tk.Frame(sites_page, bg="light grey", width=1372, height=760)
sites_frame.place(x=0, y=0)
create_sites_grid()
sites_page.withdraw()
# add site page gui
add_site_page = tk.Tk()
add_site_page.configure(bg='light blue')
add_site_page.title("Add Site")
sites_page.geometry("1000x1000")
site_entry_label = tk.Label(add_site_page, text="Enter your site")
site_entry_label.place(x=20, y=18)
site_entry = tk.Entry(add_site_page, bg='light grey')
site_entry.place(x=20, y=40)
username_entry_label = tk.Label(add_site_page, text="Enter a username or email")
username_entry_label.place(x=20, y=88)
username_entry = tk.Entry(add_site_page, bg='light grey')
username_entry.place(x=20, y=110)
password_entry_label = tk.Label(add_site_page, text="Enter a password")
password_entry_label.place(x=20, y=158)
password_entry = tk.Entry(add_site_page, bg='light grey')
password_entry.place(x=20, y=180)
add_site_submit = tk.Button(add_site_page, text="Submit", command=submit)
add_site_submit.place(x=20, y=228)
add_site_page.withdraw()

sites = []  # Tracks the list for all sites added to the page
home_page.deiconify()
home_page.mainloop()
