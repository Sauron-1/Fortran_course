for dir in ./*
do
    if test -d $dir
    then
        for file in ./$dir/*
        do
            if test -d $file
            then
                rm $file/*.exe
                rm $file/*.out
            fi
        done
    fi
done
