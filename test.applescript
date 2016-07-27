tell application "Messages"

    set targetBuddy to "+18473440965"
    set targetService to id of 1st service whose service type = iMessage

    set possibleTexts to {"neat", "cool", "great", "wow", "ye haw", "awesome"}
    set myBuddy to buddy targetBuddy of service id targetService

    repeat
    set textMessage to some item of possibleTexts
    send textMessage to myBuddy
    delay 1
    end repeat

end tell
