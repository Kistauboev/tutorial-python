def myFUNC():
    global x
    x="fantastic"
myFUNC()

print(f"Python is {x}")  #biz myFUNC() icida turgan local ni global ga uzgartirib oldik ya'ni global x va myFUNC() funksiyasini 
                         #yopdik va uning  tashqarisda print() ni ishlatdik 
                        