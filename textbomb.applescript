tell application "Messages"

    set targetBuddy to "+18477698860"
    set targetService to id of 1st service whose service type = iMessage

    set possibleTexts to {"hi", "hi bugs", "luv u", "hello", "*bug noises*", "hello bug", "I love you", "hi hi", "pbblt"}
    set myBuddy to buddy targetBuddy of service id targetService

    repeat
    send some item of possibleTexts to myBuddy
    end repeat

end tell
