# Find-largest-file-system
 Finding the largest file in drive - เนื่องจากฮาร์ดิสก์ผมพื้นที่มันค่อยๆ น้อยลงเรื่อยๆ จะหาไฟล์ขนาดใหญ่ในไดร์ฟขี้เกียจนั่งไล่หาทีละโฟลเดอร์ เลยลองทำสคริปสั้นๆ เอาไว้ดูว่าอันไหนไม่จำเป็นจะได้เข้าไปลบครับ 😁
 
 ### Installation
You need python install on your machine - เริ่มแรกให้ติดตั้ง python ก่อนครับ ถ้ายังไม่มี

วิธีติดตั้ง python on windows https://installpython3.com/windows/

### How to use

``` C:\python largefile.py ```

รันไฟล์ largefile.py ด้วย python จากนั้นกำหนดไดร์ฟหรือ path folder ที่เราต้องการค้นหา และใส่ขนาดไฟล์ขั้นต่ำที่ต้องการ

![image](https://user-images.githubusercontent.com/56244402/111025298-ca692480-8415-11eb-8dbd-da66fd23feaa.png)

เรียบร้อยตามภาพครับ ไฟล์ไหนไม่ได้ใช้ก็เข้าไปลบกันได้เลย... 😉

** การลบไฟล์บางชนิดมีความเสี่ยงที่จะทำให้ระบบ OS ใช้งานไม่ได้ ระวังลบผิดไฟล์ **

ปล. กำลังคิดไอเดียเอาไปต่อยอดทำอะไรเพิ่มได้อีก เพื่อนๆ ใครมีไอเดียเจ๋งๆ แนะนำได้นะครับ

### Adding search file name with keyword - เพิ่มการค้าหาด้วยชื่อไฟล์

![image](https://user-images.githubusercontent.com/56244402/111029239-35265a00-842e-11eb-80e6-263049fe2f21.png)

### ทดลองสร้าง GUI (ไฟล์ simply_gui.py)

```
pip install pysimplegui

pip install --upgrade PySimpleGUI 

```

![image](https://user-images.githubusercontent.com/56244402/113579020-e5fad000-964d-11eb-9013-eea2be635a3a.png)
