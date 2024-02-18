import datetime

print("Mời bạn vui lòng nhập ngày tháng năm sinh để tính tuổi")
ngàysinh = int(input("Ngày sinh:"))
thángsinh = int(input("Tháng sinh:"))
nămsinh = int(input("Năm sinh:"))

nămhiệntại = datetime.date.today().year
thánghiệntại = datetime.date.today().month
ngàyhiệntại = datetime.date.today().day

tuổinăm = nămhiệntại - nămsinh
tuổitháng = abs(thánghiệntại-thángsinh)
tuổingày = abs(ngàyhiệntại-ngàysinh)

print(" Tuổi của bạn chính xác là:", tuổinăm, " tuổi ", tuổitháng, " tháng và ", tuổingày, " ngày")