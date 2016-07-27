function zach(num)
    if num == 1 then
        return 1
    else
        return num + zach(num/2)
    end
end

print("Enter a number!")
a = io.read("*number")
print(zach(a))
