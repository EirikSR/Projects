
ACTIONS="\nActions: \nstart - start new timer\nstop - stops timer \nstatus - get task name\nabort - exit program\nlog - display taskes + elapsed time HH:MM:SS\n"
echo "Welcome to the timer!"
printf "$ACTIONS" #Posible actions are stored as a string

run=false #True if timer is running, false if not
LOGFILE=".local/share/log.txt"
while true; do #Loop to contain the program
read input
VALID_INPUT=false #In order to check for non-actions

if [ input != "" ]; then #Actions here

    if [ "$input" = "start" ]; then #Starts timer
        VALID_INPUT=true
        if [ "$run" = false ]; then
            echo "Welcome to timer, what task is being timed?"
            read LABEL
            echo "Press enter to start timer"
            read starter
            START=$(date -u) #Date in correct format for log
            echo "Timer started at:" $START
            run=true
        else
            echo "Error, timer already running"
        fi
    fi

    if [ "$input" = "stop" ]; then #Stops the timer, adds instance to log
        VALID_INPUT=true
        if [ "$run" = true ]; then
            STOP=$(date -u) #Date in correct format for log
            echo "Timer started at:" $STOP
            echo "START" $START >> $LOGFILE
            echo "LABEL" $LABEL >> $LOGFILE
            echo "STOP" $STOP >> $LOGFILE
            echo "" >> $LOGFILE
            echo "Log updated"
            run=false
        else
            echo "Error, no timer running"
        fi
    fi

    if [ "$input" = "status" ]; then #Suplies status, start time if timer is active, message otherwise
        VALID_INPUT=true
        if [ $run = true ]; then
            
            echo "Task" $label "is running, started at" $START
        else
            echo "No task currently running"
        fi
    fi

    if [ "$input" = "abort" ]; then #Simply aborts timer, nothing stored in log
        VALID_INPUT=true
        echo "Timer aborted"
        break
    fi

    if [ "$input" = "log" ]; then #Writing the log from file
        VALID_INPUT=true

        LOG_DATA=() #Empty array
        while IFS= read -r line; do
            LOG_DATA+=("Text read from file: $line") #adds each line from file to array
        done < $LOGFILE
        alenght=${#LOG_DATA[@]} #Length of array for for-loop
        
        for (( i=0; i<${alenght}; i+=4 ));do #each log input is 4 lines
            #for further finesse it could be smart to check that first line is the START time
            a="${LOG_DATA[i]}"
            b="${LOG_DATA[i+1]}"
            c="${LOG_DATA[i+2]}"
            d="${LOG_DATA[i+3]}"
            a=${a:27}
            b=${b:26}
            c=${c:25}
            a=$(date -d"$a" +%s) #Converts date to seconds (since 1970)
            c=$(date -d"$c" +%s)
            TIME_ELAPS=$(($c - $a)) #Finds elapsed seconds
            TIME_ELAPS=$(date -d@$TIME_ELAPS -u +%H:%M:%S) #Converts seconds to HH:MM:SS
            echo $b $TIME_ELAPS
        done

    fi

    if [ $VALID_INPUT = false ]; then #Rewrites the action list if input does not mach
        echo "No valid argument detected"
        printf "$ACTIONS"
    fi

fi

done
