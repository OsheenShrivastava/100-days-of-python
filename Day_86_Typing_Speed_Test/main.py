# Initialization and canvas
# TODO-1 - Import pandas as pd
# TODO-2 - Create a csv file and add 1 to 100 words alphabetically.
# TODO-3 - Read the csv file by defining header as None and define column name "word" for words column.
# TODO-4 - Import all from tkinter. Also import messagebox. Create a window object, add title and define its size.
# TODO-5 - Create a canvas of the same size as that of window and place it at (0,0).
# TODO-6 - Create a Text named Random_Words_Generator. Create canvas window, align it at (50,50) with anchor as "nw".
#  Add window name as Random_Words_Generator.
# TODO-7 - Create Text Box using Entry to enter user's text.
# TODO-8 - Add text for Time Left, Corrected CPM, Words Per Minute, Your Score and Best Score.
# TODO-9 - Create labels to store the readings for the above parameters.
# TODO-10 - Call load_last_score() function to load last score and store it in last_score variable. Add the last_score
#  to Last_Score_Value label.
# TODO-11 - Create Restart_Button to start the timer and run typing_test program again. Add command
#  lambda: Generate_Random_Words(). Normal command stores the callable you give it and calls it later when the button
#  is clicked and no arguments can be passed in this. Whereas, lambda function will Call the function only later
#  (not at creation), Pass arguments to the function when the button is clicked and Freeze the current value of a loop
#  variable.
# TODO-12 - Create Reset_Button to reset Best Score. Pass reset_best_score() function as command.
# TODO-13 - Configure tags of Random_Words_Generator. There are 5 of them.
#  current_word = foreground="black", background="lightgreen"
#  typed_char = foreground="white", background="lightgreen"
#  wrong_char = foreground="red", background="lightgreen"
#  correct_word = foreground="green", background="white"
#  incorrect_word = foreground="red", background="white"
# TODO-14 - When multiple tags are applied to same chunk of text then we use raise and lower functions. raise() moves a
#  tag above others. lower() moves a tag below others. Here "typed_char" and "wrong_char" are raised above
#  "current_word".
# TODO-15 - To run the timer create a bind "<KeyRelease>" function to Text_Box which will call an event if a key is
#  released. Calls your function after a key is released. Useful if you want the typed text already updated in the
#  Entry (Text_Box.get() will include the last key). Example: If you press a, the function runs when you let go of the
#  key, and "a" is already in the entry.
# TODO-16 - Call Generate_Random_Words() function to generate random words in the Random_Words_Generator Text Window.



#  Generate random words
# TODO-17 - Initialize them at the start of the program --> words_list = [], word_positions = [],
#  line_word_indices = [], lines_visible = 7, words_per_line = 6, next_word_index = 0, visible_lines = [],
#  visible_indices = [], mapping = {}, finalized = {} and SEP = "  ".
# TODO-18 - Create a function Generate_Random_Words(). Add global variables correct_chars, typed_words, start_time,
#  Time_Elapsed, timer_running, timer_id,words_list, word_positions, line_word_indices, next_word_index,
#  current_word_index, visible_lines, visible_indices, mapping, finalized.
# TODO-19 - Initialize these variables --> visible_lines = [], visible_indices = [], mapping = {}, line_num = 1 and
#  next_word_index = 0.
#  This function runs each time we refresh or generate new words for the typing test — such as: When you start a new
#  round, When the timer resets, When the user completes the current word set. Its purpose is to: Create a fresh block
#  of words and Reset all tracking lists that depend on those words.
# TODO-20 - Inside Generate_Random_Words() function check if timer_id is not None, then cancel the timer and again set
#  it to None. This is done so that when timer resets when restart button is pressed.
# TODO-21 - Reset all stats --> correct_chars = 0, typed_words = 0, start_time = 60, Time_Elapsed = 0,
#  timer_running = False, current_word_index = 0, finalized = {}.
# TODO-22 - Config the tags to their default value. Time_Left_Value = "60", Corrected_CPM_Value = "0",
#  Words_Per_Minute_Value = "0", Your_Score_Value.config = "0".
# TODO-23 - Create a variable named data. Read words csv, make sure header is none and give column heading "word".
# TODO-24 - Drop NaN (missing/empty values) using dropna(), convert all values to strings using astype(str) and finally
#  convert the series to list.
# TODO-25 - Import random and shuffle all words and store then in a variable words_list.
# TODO-26 - A FOR loop is used to select and group the next few words from words_list into multiple visible lines for
#  the typing test display — for example, if you only show 4 lines at a time in your Text widget.
# TODO-27 - This is used for splitting word indices into lines. chunk takes a slice (a small group) of words from the
#  main words_list. Suppose words_list = ["dog", "runs", "fast", "in", "the", "park", "every", "day"]
#  And next_word_index = 0, words_per_line = 4. Then chunk = ["dog", "runs", "fast", "in"]
# TODO-28 - If you’ve reached the end of the word list (no more words left), stop looping early i.e., break.
# TODO-29 - indices_chunk Creates a list of indices corresponding to the words in that chunk.
#  For the above example: indices_chunk = [0, 1, 2].
#  If the next line starts at word index 3, then it would become [3, 4, 5], etc.
#  These indices help track which words belong to which line — useful for highlighting and scrolling.
# TODO-30 - visible_lines.append(chunk) stores the actual words for this visible line, e.g.
#  visible_lines = [["dog", "runs", "fast", "in"], ["the", "park", "every", "day"]]
# TODO-31 - visible_indices.append(indices_chunk) stores the indices for that line’s words, e.g.
#  visible_indices = [[0, 1, 2], [3, 4, 5]]. These are useful when mapping cursor positions or highlighting.
# TODO-32 - next_word_index += len(chunk) moves the starting index forward for the next line. So next time the slice
#  picks up from where the previous line ended.
#  For example:
#  Before: next_word_index = 0
#  After 1st iteration: next_word_index = 3
#  After 2nd iteration: next_word_index = 6
# TODO-33 - Call Render_Visible() function.
# TODO-34 - Delete all the data in Text_Box and focus the cursor so that it is ready to receive keyboard input.
# TODO-35 - Create a function named Highlight_Current_Word() and call it after Text_Box focus.



# render_visible
# TODO-36 - Add global variable mapping. Config Random_Words_Generator label with state=NORMAL so that new random words
#  can be entered (it means that text box is editable now). Use delete function from "1.0" i.e., first character to END
#  to delete all the words.
# TODO-37 - Initialize varaibles mapping and line_num.
# TODO-38 - Initialize FOR loop and iterate over lists of visible_lines(4) and visible_indices(words per line 6).
# TODO-39 - Join words using separator ("  ") and insert that line into the Text widget. If line_num < visible_lines
#  then it inserts a new line between lines.
# TODO-40 - Now we will calculate word position. Iterate over each word in the line and figure out where that word
#  appears inside the line of text being inserted. char_offset keeps track of how many characters we’ve already written
#  in the current line.
# TODO-41 - for idx_in_line, w in enumerate(line_words): enumerate(line_words) gives both the index and the word. Index
#  to look up the global word index, and the word (w) itself for display/measurement.
# TODO-42 - This global_idx uniquely identifies each word in the entire text block, not just the current line — which is
#  how your program later knows: which word was typed (current_word_index) and where to apply highlights
#  (via mapping[global_idx]).
# TODO-43 - Calculate the start and end position of that word. Save all the info in mapping.
#  For e.g. - Start pos=0.
#  "apple" → start at 0, length = 5 → next pos = 5+2=7.
#  "banana" → start at 7, length = 6 → next pos = 15.
#  "cherry" → start at 15, length = 6 → next pos = 23.
#  "date" → start at 23, length = 4 → next pos = 29.
#  "fig" → start at 29, length = 3 → next pos = 34.
#  "grape" → start at 34, length = 5 → next pos = 41.
#  "kiwi" → start at 41, length = 4 → next pos = 47.
#  So: word_positions t = [0, 7, 15, 23, 29, 34, 41]. This is useful for highlighting words later. Store line,
#  start_char, end_char, start_idx and end_idx in mapping.
# TODO-44 - After each word, you move the character pointer forward: So the next word starts right after the separator.
# TODO-45 - After all words in the line move to the next line in the text widget by incrementing line_num by 1.
# TODO-46 - Run a FOR loop in mapping items where gidx = global word index (like 0, 1, 2) and info = a dictionary with
#  the start and end positions of that word. finalized is another dictionary that stores whether each word has been
#  typed correctly or incorrectly before.
# TODO-47 - Check if the words are correct or incorrect and it to Random_Words_Generator. Configure the tags for both.
# TODO-48 - Finally config the state=DISABLED to lock the text box from editing (read-only).
# TODO-49 - tag_raise("typed_char") brings typed characters to top, tag_raise("wrong_char") brings wrong characters to
#  top and tag_lower("current_word") pushes current word highlight to bottom.



# highlight current words
# TODO-50 - Removes the tag "current_word" everywhere in the text widget (from beginning "1.0" to end). This clears the
#  previous highlight before applying a new one.
# TODO-51 - current_word_index is a global index that tracks which word the user is typing. mapping is a dictionary
#  (created in Generate_Random_Words()) that stores the Tkinter start and end positions of every visible word.
# TODO-52 - Apply the tag to current_word to highlight it using the start and end positions.
# TODO-53 - tag_raise functions is used to highlight both the typed character green and wrong letter red appears on the
#  top of the highlight colour. Without this, highlight color may cover the characters.



#  On Key release
# TODO-54 - Create On_Key_Press function to run when a key is pressed in the Text_Box. Add global variables
#  current_word_index, typed_words, correct_chars, timer_running, start_time, next_word_index, last_score.
# TODO-55 - Inside On_Key_Press() function create a variable typed_text and store data from Textbox to it.
# TODO-56 - Create a variable timer_running and set it to false by default.
# TODO-57 - Check if timer is not running and text typed by user is something and not just spaces. Strip() removes
#  leading and trailing spaces. If yes, then start the timer,set timer_running to true and call Show_Elapsed_Time() to
#  display the time.
# TODO-58 - If the user has already typed all words, just stop.
# TODO-59 - mapping is a dictionary that stores where each word is located inside the Text widget. Get position info for
#  the current word by passing current_word_index in mapping.get() function and store it in info.
# TODO-60 - If word is not found then call Render_Visible() which draws words on screen and rebuilds the mapping. After
#  that, it tries to get the word location again.
# TODO-61 - Obtain start index and end index of the current_word from info which receives it from mapping.
# TODO-62 - Clear old per-character highlights for typed and wrong chracter. This is required so that they don’t stack.
# TODO-63 - When the user presses space key or ' '. hasattr(event, "char") ensures .char exists. take what they typed,
#  strip it and store in variable fragment.
# TODO-64 - Compare it with the actual word. If true then increment typed_words with 1 and correct_chars with length of
#  the current_word/fragment.
# TODO-65 - If correct → store "correct" in finalized[current_word_index] and config whole word with "correct_word".
#  If wrong → store "incorrect" in finalized[current_word_index] and config whole word with "incorrect_word". Use
#  start_idx and end_idx for this.
# TODO-66 - Store the line number of the word we just finalized (before advancing index). Move to next word by
#  incrementing current_word_index with 1. Clear the Text_Box.
# TODO-67 - Next we will design a text scroller. When user finishes typing a word that is located on the second-last
#  visible line, it checks if that was the last word on that line. If yes --> scroll the text up and load a new line.
#  if word_line == (lines_visible - 1): Check if the typed word was on the second-last visible line.
#  visible_indices[word_line - 1]: Get the list of all word positions (indexes) on that line. indices_in_line: Stores
#  which words belong to that line. word_line - 1 < len(visible_indices): Check if that line exists in the list.
#  visible_indices[word_line - 1]	If it exists → use that line's word indices. else []: If it doesn’t exist → return
#  empty list (safe fallback). if indices_in_line and current_word_index > indices_in_line[-1]: Check if the user just
#  completed the last word on that line. Call scroll_one_line_and_add_new() to scroll the text up and display a new
#  line of words.
# TODO-68 - Call Highlight_Current_Word() to highlight the next word. Call Update_Stats() to update CPM,WPM and
#  Final_Score.
# TODO-69 - For Live per-character highlighting, get curr_word from words_list using current_word_index.
# TODO-70 - Use FOR loop for per-character highlighting along with enumerate() function. enumerate() gives you both the
#  index (i) and the character (ch).
#  Example: if user typed "apx", then:
#  i=0, ch="a"
#  i=1, ch="p"
#  i=2, ch="x"
# TODO-71 - Check if index is still inside the word. Ensures we don’t go out of bounds.
#  Example: current_word = "apple", so length = 5. If user typed "applexyz" (7 chars), i=5,6 will be outside.
# TODO-72 - Calculate start of the character using current line number and starting column of the word where i is the
#  current character position inside the word. So exact position of letter is calculated. char_end is the next next
#  character after the char_start so "i+1".
# TODO-73 - Compares typed character with the correct character at same position. If correct → apply "typed_char" tag
#  i.e., text color = white and background = green. If mismatch, highlight with "wrong_char" with text colour = red.
# TODO-74 - If the user keeps typing after the word length (extra chars beyond word), mark the whole word wrong.



#  Show_Elapsed_Time
# TODO-75 - Inside Show_Elapsed_Time() add global variables start_time, timer_running, timer_id and last_score where
#  start_time = 60 and timer_running = true by default.
# TODO-76 - This function is responsible to display real time readings of 60 secs timer. Inside this function check
#  if start_time > 0 and timer_running is true, if yes then config the Time_Left_Value to display time, add a delay of
#  1 sec and decrement the start_time by 1.
# TODO-77 - Else if timer is still running and start_time is no more greator then 0, it will check else condition.
#  In this it will display text as 0 i.e., timer over and set time_running to False.
# TODO-78 - Store the elapsed time of timer in this timer_id so that we can cancel the timer using this timer_id.
#  Tkinter assigns a unique job id to every tasks so that it can we used to schedule a task in future. In the elif
#  condition set timer_id = None.
# TODO-79 - Get final_wpm from Words_Per_Minute_Value label. Compare this final_wpm with last_score where last_score is
#  initialized as 0 at the start. If final_wpm is greator than last_score then save final_wpm as last_score. Call
#  Save_Last_Score() function and pass last_score value to it to save it. Here Last_Score_Value is nothing but your
#  Best_Score.
# TODO-80 - Also update Last_Score_Value label with last_score value. Here try/except is used to ignore errors if the
#  label isn't available.
# TODO-81 - messagebox pops up when timer is over to show user's current WPM and Best_score value.


# scroll_one_line_and_add_new
# TODO-82 - This function is responsible for - Removing the top visible line
#  Adding a new line from words_list at the bottom
#  Keeping visible_lines and visible_indices updated
#  Re-renders the text display using Render_Visible()
# TODO-83 - Here visible_lines → Currently displayed lines of words, visible_indices → Word indices corresponding to
#  each line and next_word_index → Tracks from where to fetch the next batch of words. if nothing is displayed, exit
#  the function.
# TODO-84 - visible_lines.pop(0) and visible_indices.pop(0) - Removes the first (top) line from the screen — Like
#  scrolling up.
# TODO-85 - Next we nee to append a frsh line from the words_list to display at the bottom.
#  if next_word_index < len(words_list): Checks if there are still more words left to show.
# TODO-86 - new_chunk = words_list[next_word_index: next_word_index + words_per_line]: TakeS the next group of words
#  (one line) from the word list.
# TODO-87 - if new_chunk: Safety check – only proceed if new words exist.
# TODO-88 - idx_chunk = list(range(next_word_index, next_word_index + len(new_chunk))): Creates a list of indices
#  (positions) for those words in the main list. E.g.: if we take words at positions 12,13,14 → idx_chunk = [12,13,14].
# TODO-89 - visible_lines.append(new_chunk): Add the new words as a visible line on screen.
# TODO-90 - visible_indices.append(idx_chunk): Store the index mapping so we know exactly which word is where. Useful to
#  track correctness, highlight, etc.
# TODO-91 - next_word_index += len(new_chunk): Moves the pointer forward to prepare for the next scroll.
# TODO-92 - In else condition, if there are no more words, append an empty line to keep line count stable so
#  visible_lines.append([]) and visible_indices.append([]) are used.
# TODO-93 - Finally call Render_Visible() function to re-render the entire visible area so the user sees updated text.



# Update_State
# TODO-94 - Check time elapsed to calculate WPM and CPM. If time elapsed is greater then 0 then calculate WPM and CPM
#  else set them to 0.
# TODO-95 - WPM = typed_words * (60 / Time_Elapsed) and CPM = correct_chars * (60 / Time_Elapsed). Configure both to
#  their respective labels.
# TODO-96 - Also config user score named Your_Score_Value which is same as that of WPM.



# Save_Last_Score
# TODO-97 - Open file named "best_score.txt" in write mode "w" as "f". If the file doesn’t exist, it will be created.
#  If it exists, it will be overwritten.
# TODO-98 - Convert the score to a string and write it into the file.



# Load_Last_Score
# TODO-99 - This function is designed to load the previously saved best score from the file best_score.txt. Opens the
#  file in read mode "r".
# TODO-100 - Reads the entire content and removes extra spaces or newline characters. Converts the content into an
#  integer (your score).
# TODO-101 - except FileNotFoundError: Handles case when file does not exist (e.g., first run).
#  except ValueError: Handles case when the file content is not a valid number (corrupt or empty). return 0: If
#  anything goes wrong, return 0 as default score.



# Reset_Best_Score
# TODO-102 - This function resets the saved best score to 0, updates the UI labels, and informs the user. last_score is
#  declared as global.
# TODO-103 - Shows a confirmation popup (Yes / No). If the user clicks No, the function stops (return).
# TODO-104 - Call Save_Last_Score(0) to write 0 into best_score.txt. Updates the in-memory variable last_score = 0.
# TODO-105 - Config Last_Score_Value label with last_score. Wrapped in try/except to avoid errors if label doesn't
#  exist.
# TODO-106 - Reset Your_Score_Value, Words_Per_Minute_Value and Corrected_CPM_Value labels. Use try/except to avoid
#  errors.
# TODO-107 - Shows confirmation popup that reset is successful. Add an exception if something goes wrong. Show an error
#  message with details.






import pandas as pd
import random
from tkinter import *
from tkinter import messagebox

start_time = 60
timer_running = False
correct_chars = 0
Time_Elapsed = 0
typed_words = 0
timer_id = None

words_list = []          # master list of all words
word_positions = []      # positions of words in Text widget
line_word_indices = []   # indices of words per line in the Text widget
lines_visible = 5        # number of visible lines in Text widget
words_per_line = 5       # approximate words per line
next_word_index = 0      # index in master words_list for new words
current_word_index = 0   # current word being typed

visible_lines = []        # list of lists of words currently visible
visible_indices = []      # list of lists of global indices for each visible line
mapping = {}              # mapping: global_index -> dict(line, start_char, end_char)
finalized = {}            # global_index -> "correct" / "incorrect" for persistent styling
SEP = "  "   # spacing between words (two spaces like your original)

last_score = 0




def Save_Last_Score(score):
    with open("best_score.txt", "w") as f:
        f.write(str(score))



def Load_Last_Score():
    try:
        with open("best_score.txt", "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0



def Reset_Best_Score():
    """Reset stored best score to 0 and update UI."""
    global last_score
    answer = messagebox.askyesno("Reset Best Score", "Are you sure you want to reset the best score to 0?")
    if not answer:
        return
    try:
        Save_Last_Score(0)
        last_score = 0
        # Update UI labels (safe-guard if they exist)
        try:
            Last_Score_Value.config(text=str(last_score))
        except:
            pass
        try:
            Your_Score_Value.config(text="0")
            Words_Per_Minute_Value.config(text="0")
            Corrected_CPM_Value.config(text="0")
        except:
            pass
        messagebox.showinfo("Reset", "Best score has been reset to 0.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to reset best score: {e}")



def Update_Stats():
    Time_Elapsed = 60 - start_time
    if Time_Elapsed > 0:
        WPM = typed_words * (60 / Time_Elapsed)
        CPM = correct_chars * (60 / Time_Elapsed)
    else:
        WPM = 0
        CPM = 0
    Words_Per_Minute_Value.config(text=f"{int(WPM)}")
    Corrected_CPM_Value.config(text=f"{int(CPM)}")
    Your_Score_Value.config(text=f"{int(WPM)}")



def Render_Visible():
    """
    Render visible_lines into the Text widget and rebuild mapping of global index -> start/end positions.
    """
    global mapping

    Random_Words_Generator.config(state=NORMAL)
    Random_Words_Generator.delete("1.0", "end")

    mapping = {}
    line_num = 1

    for line_words, line_indices in zip(visible_lines, visible_indices):
        line_text = SEP.join(line_words)
        Random_Words_Generator.insert(END, line_text)
        if line_num < lines_visible:
            Random_Words_Generator.insert(END, "\n")

        # compute per-word start/end char offsets for this line
        char_offset = 0
        for idx_in_line, w in enumerate(line_words):
            global_idx = line_indices[idx_in_line]
            start_idx_str = f"{line_num}.0+{char_offset}c"
            end_idx_str = f"{line_num}.0+{char_offset + len(w)}c"
            mapping[global_idx] = {
                "line": line_num,
                "start_char": char_offset,
                "end_char": char_offset + len(w),
                "start_idx": start_idx_str,
                "end_idx": end_idx_str
            }
            # add length and separator (not after last word)
            if idx_in_line < len(line_words) - 1:
                char_offset += len(w) + len(SEP)
            else:
                char_offset += len(w)
        line_num += 1

    # re-apply persistent finalized tags (correct/incorrect) for words still visible
    for gidx, info in mapping.items():
        status = finalized.get(gidx)
        if status == "correct":
            Random_Words_Generator.tag_add("correct_word", info["start_idx"], info["end_idx"])
        elif status == "incorrect":
            Random_Words_Generator.tag_add("incorrect_word", info["start_idx"], info["end_idx"])

    Random_Words_Generator.config(state=DISABLED)

    # Ensure tag stacking: typed/wrong override current_word background
    Random_Words_Generator.tag_raise("typed_char")
    Random_Words_Generator.tag_raise("wrong_char")
    Random_Words_Generator.tag_lower("current_word")



def Highlight_Current_Word():
    Random_Words_Generator.tag_remove("current_word", "1.0", "end")
    info = mapping.get(current_word_index)
    if info:
        Random_Words_Generator.tag_add("current_word", info["start_idx"], info["end_idx"])
        # make sure typed/wrong chars are above it
        Random_Words_Generator.tag_raise("typed_char")
        Random_Words_Generator.tag_raise("wrong_char")



def Generate_Random_Words():
    global correct_chars, typed_words, start_time, Time_Elapsed, timer_running, timer_id, words_list, word_positions
    global line_word_indices, next_word_index, current_word_index, visible_lines, visible_indices, mapping, finalized

    visible_lines = []
    visible_indices = []
    mapping = {}
    next_word_index = 0

    # Cancel any running timer
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None

    # Reset stats
    correct_chars = 0
    typed_words = 0
    start_time = 60
    Time_Elapsed = 0
    timer_running = False
    current_word_index = 0
    finalized = {}

    Time_Left_Value.config(text="60")
    Corrected_CPM_Value.config(text="0")
    Words_Per_Minute_Value.config(text="0")
    Your_Score_Value.config(text="0")

    # Load words from CSV
    data = pd.read_csv('words.csv', header=None, names=['word'])
    all_words = data['word'].dropna().astype(str).tolist()
    random.shuffle(all_words)
    words_list = all_words

    for _ in range(lines_visible):
        chunk = words_list[next_word_index: next_word_index + words_per_line]
        if not chunk:
            break
        indices_chunk = list(range(next_word_index, next_word_index + len(chunk)))
        visible_lines.append(chunk)
        visible_indices.append(indices_chunk)
        next_word_index += len(chunk)

    Render_Visible()

    # Clear entry and focus
    Text_Box.delete(0, END)
    Text_Box.focus_set()

    # Highlight first word
    Highlight_Current_Word()



def scroll_one_line_and_add_new():
    """
    Remove the top visible line and append a fresh line from words_list (if available).
    Re-render everything and keep mapping accurate.
    """
    global visible_lines, visible_indices, next_word_index

    if not visible_lines:
        return

    # pop top line
    visible_lines.pop(0)
    visible_indices.pop(0)

    # append new line
    if next_word_index < len(words_list):
        new_chunk = words_list[next_word_index: next_word_index + words_per_line]
        if new_chunk:
            idx_chunk = list(range(next_word_index, next_word_index + len(new_chunk)))
            visible_lines.append(new_chunk)
            visible_indices.append(idx_chunk)
            next_word_index += len(new_chunk)
    else:
        # if no more words, append an empty line to keep line count stable
        visible_lines.append([])
        visible_indices.append([])

    Render_Visible()



def On_Key_Release(event):
    global current_word_index, typed_words, correct_chars, timer_running, start_time, next_word_index, last_score

    typed_text = Text_Box.get()

    # Start timer
    if not timer_running and typed_text.strip() != "":
        timer_running = True
        Show_Elapsed_Time()

    if current_word_index >= len(words_list):
        return

    # ensure mapping exists for current word
    info = mapping.get(current_word_index)
    if not info:
        # current word not visible (rare) — try to render visible region so mapping updates
        Render_Visible()
        info = mapping.get(current_word_index)
        if not info:
            return

    start_idx = info["start_idx"]
    end_idx = info["end_idx"]

    # Remove previous live highlights
    Random_Words_Generator.tag_remove("typed_char", start_idx, end_idx)
    Random_Words_Generator.tag_remove("wrong_char", start_idx, end_idx)

    # If space pressed -> finalize the word
    if (event.keysym == 'space') or (hasattr(event, "char") and event.char == ' '):
        fragment = typed_text.strip()

        if fragment == words_list[current_word_index]:
            typed_words += 1
            correct_chars += len(fragment)
            finalized[current_word_index] = "correct"
            Random_Words_Generator.tag_add("correct_word", start_idx, end_idx)
        else:
            finalized[current_word_index] = "incorrect"
            Random_Words_Generator.tag_add("incorrect_word", start_idx, end_idx)

        # store the line number of the word we just finalized (before advancing index)
        word_line = info["line"]

        current_word_index += 1
        Text_Box.delete(0, END)

        # If we finalized a word on the 2nd last visible line → scroll up one line
        # (line numbers are 1..LINES_VISIBLE)
        # We check whether the finished word was the last in that 2nd-last line.

        if word_line == (lines_visible - 1):
            # indices for that line (global indices)
            indices_in_line = visible_indices[word_line - 1] if word_line - 1 < len(visible_indices) else []
            if indices_in_line and current_word_index > indices_in_line[-1]:
                scroll_one_line_and_add_new()

        Highlight_Current_Word()
        Update_Stats()
        return

    # Live per-character highlighting
    cur_word = words_list[current_word_index]
    for i, ch in enumerate(typed_text):
        if i < len(cur_word):
            char_start = f"{info['line']}.0+{info['start_char'] + i}c"
            char_end = f"{info['line']}.0+{info['start_char'] + i + 1}c"
            if ch == cur_word[i]:
                Random_Words_Generator.tag_add("typed_char", char_start, char_end)
            else:
                Random_Words_Generator.tag_add("wrong_char", char_start, char_end)
        else:
            # typed extra characters beyond word => mark entire word wrong visually
            Random_Words_Generator.tag_add("wrong_char", start_idx, end_idx)


def Show_Elapsed_Time():
    global start_time, timer_running, timer_id, last_score
    if start_time > 0 and timer_running:
        Time_Left_Value.config(text=f"{start_time}")
        timer_id = window.after(1000, Show_Elapsed_Time)
        start_time -= 1
    elif timer_running:
        Time_Left_Value.config(text="0")
        timer_running = False
        timer_id = None

        final_wpm = int(Words_Per_Minute_Value.cget("text"))

        # --- Compare with last_score and save if better ---
        if final_wpm > last_score:
            last_score = final_wpm
            Save_Last_Score(last_score)

        # Update Last score label if present
        try:
            Last_Score_Value.config(text=str(last_score))
        except:
            pass

        messagebox.showinfo("Time up!", f"Time's up!\nYour WPM: {final_wpm}\nBest Score: {last_score}")





window = Tk()
window.title("Typing Speed Test")
window.geometry("800x450")
window.resizable(False, False)
canvas = Canvas(window, width=800, height=450)
canvas.place(x=0, y=0)

Random_Words_Generator = Text(window, width=40, height=5, font=("Arial", 14), bg="white", fg="black",
                               relief="groove", wrap="word", spacing2=5)
canvas.create_window(50, 50, anchor="nw", window=Random_Words_Generator)

Text_Box = Entry(window, width=40, font=("Arial", 14), bg="white", fg="black", relief="groove")
canvas.create_window(50, 360, anchor="nw", window=Text_Box)

canvas.create_text(600, 70, text="Time Left :", font=("Arial", 13), fill="black", anchor="center")
canvas.create_text(600, 130, text="Corrected CPM :", font=("Arial", 13), fill="black", anchor="center")
canvas.create_text(600, 190, text="Words Per Minute :", font=("Arial", 13), fill="black", anchor="center")
canvas.create_text(600, 250, text="Your Score :", font=("Arial", 13), fill="black", anchor="center")
canvas.create_text(600, 310, text="Best Score :", font=("Arial", 13), fill="black", anchor="center")

Time_Left_Value = Label(window, text="60", font=("Arial", 13), bg="white", width=4, height=1)
canvas.create_window(730, 70, anchor="center", window=Time_Left_Value)

Corrected_CPM_Value = Label(window, text="0", font=("Arial", 13), bg="white", width=4, height=1)
canvas.create_window(730, 130, anchor="center", window=Corrected_CPM_Value)

Words_Per_Minute_Value = Label(window, text="0", font=("Arial", 13), bg="white", width=4, height=1)
canvas.create_window(730, 190, anchor="center", window=Words_Per_Minute_Value)

Your_Score_Value = Label(window, text="0", font=("Arial", 13), bg="white", width=4, height=1)
canvas.create_window(730, 250, anchor="center", window=Your_Score_Value)

last_score = Load_Last_Score()
Last_Score_Value = Label(window, text=str(last_score), font=("Arial", 13), bg="white", width=4, height=1)
canvas.create_window(730, 310, anchor="center", window=Last_Score_Value)

Restart_Button = Button(window, text="Restart", height=1, width=35, command=Generate_Random_Words)
canvas.create_window(650, 371, window=Restart_Button)

Reset_Button = Button(window, text="Reset_Best", height=1, width=35, command=Reset_Best_Score)
canvas.create_window(650, 410, window=Reset_Button)

# Tag styles
Random_Words_Generator.tag_configure("current_word", foreground="black", background="lightgreen")
Random_Words_Generator.tag_configure("typed_char", foreground="white", background="lightgreen")
Random_Words_Generator.tag_configure("correct_word", foreground="green", background="white")
Random_Words_Generator.tag_configure("incorrect_word", foreground="red", background="white")
Random_Words_Generator.tag_configure("wrong_char", foreground="red", background="lightgreen")

Random_Words_Generator.tag_raise("typed_char")
Random_Words_Generator.tag_raise("wrong_char")
Random_Words_Generator.tag_lower("current_word")

Text_Box.bind("<KeyRelease>", On_Key_Release)

Generate_Random_Words()

window.mainloop()