tell application "Messages"

    set targetBuddy to "+18479618261"
    set targetService to id of 1st service whose service type = iMessage

    set possibleTexts to {"hey", "hey care", "wake up", "care wake up", "ye haw", "hey care wake up", "care bear", "big care", "caroline", "caroline wake up", "care get woke"}
    set myBuddy to buddy targetBuddy of service id targetService

    repeat
    send some item of possibleTexts to myBuddy
    delay 1
    end repeat

end tell
