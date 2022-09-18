# import

# class StartMenuView:
#     def start_menu_view():
#         screen.fill(BLACK)
#         # main title
#         tetris_title = my_font(300).render("Tetris", True, CREAM)
#         title_rect = tetris_title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.15))
#         screen.blit(tetris_title, title_rect)

#         # year + course code
#         course_info = "Made for:\n3815ICT\nSoftware Engineering\nYear: 2022"
#         write_lines(screen, course_info, my_font(35), ORANGE, SCREEN_WIDTH*0.01, SCREEN_HEIGHT*0.5)
#         # student names
#         student_names = "Students:\nPaul Smyth\nKevin Pho\nRobert Newcombe\nEmanuel Worku"
#         write_lines(screen, student_names, my_font(35), ORANGE, SCREEN_WIDTH*0.01, SCREEN_HEIGHT*0.65)

#         # instantiating buttons
#         play_button = Button("PLAY!", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.40), my_font(200), CREAM)
#         options_button = Button("Settings", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.6), my_font(100), CREAM)
#         # credits_button = Button("Credits", (SCREEN_HEIGHT/2, SCREEN_HEIGHT*0.6), my_font(70), CREAM)
#         score_button = Button("High Scores", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.75), my_font(100), CREAM)
#         exit_button = Button("Exit", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.9), my_font(80), CREAM)

#         # for blitting buttons to screen
#         buttons = [play_button, options_button, exit_button, score_button]
#         for button in buttons:
#             button.update(screen)