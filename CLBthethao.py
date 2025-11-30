from guizero import App,Box, Text, PushButton,TextBox,Slider,Combo,ButtonGroup,info
app=App(title='CLB Thể Thao', width=1000, height=800)
box=Box(app,layout='grid')
box1=Box(app,layout='grid')
box2=Box(app,layout='grid')
box3=Box(app,layout='grid')
box4=Box(app,layout='grid')
box5=Box(app,layout='grid')
text=Text(box, text='Họ và tên:',grid=[0,0])
text=Text(box1, text='Chọn cấp học',grid=[0,0])
text=Text(box2, text='Chọn chiều cao (cm)',grid=[0,0])
text=Text(box3, text='Email:',grid=[0,0])
text=Text(box4, text='Số điện thoại:',grid=[0,0])
text=Text(box5, text='Chọn giới tính:',grid=[0,0])
hovaten=TextBox(box,width=30,grid=[1,0])
caphoc=Combo(box1,options=['TH','THCS','THPT'],grid=[1,0])
chieucao=Slider(box2,start=100,end=300,grid=[1,0])
email=TextBox(box3,text='@gmail.com',width=30,grid=[1,0])

sdt=TextBox(box4,width=20,grid=[1,0])
gioitinh=ButtonGroup(box5,options=['Nam','Nữ','Khác'],horizontal=True,grid=[1,0])
def dangki():
    if hovaten.value=='':
        info('Bạn chưa nhập đủ các yêu cầu, cần xem lại')
    if email.value=='':
        info('Bạn chưa nhập đủ các yêu cầu, cần xem lại')
    if sdt.value=='':
        info('Bạn chưa nhập đủ các yêu cầu, cần xem lại')
    if sdt.value!=0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        info('Số điện thoại không hợp lệ, vui lòng nhập lại')
    else:
        info('Đăng kí thành công')
nutdangki=PushButton(app,text='Đăng kí',command=dangki)
app.display()
