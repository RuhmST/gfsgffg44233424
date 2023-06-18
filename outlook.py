import getpass
import imaplib

# Hotmail 邮箱 IMAP 服务器的主机名和端口
host = 'imap-mail.outlook.com'
port = 993

# 提示用户输入邮箱账号和密码（格式：账号——密码）
account = input("请输入 Hotmail 邮箱账号和密码（格式：账号——密码）: ")
username, password = account.split('——')

# 连接到 Hotmail 邮箱服务器
imap_server = imaplib.IMAP4_SSL(host, port)
imap_server.login(username, password)

# 选择邮箱文件夹（如 INBOX）
imap_server.select("INBOX")

# 搜索邮件
status, data = imap_server.search(None, "ALL")
email_ids = data[0].split()

# 遍历邮件
for email_id in email_ids:
    # 获取邮件内容
    status, data = imap_server.fetch(email_id, "(RFC822)")
    raw_email = data[0][1].decode("utf-8")
    email_content = raw_email.split("\r\n\r\n", 1)[1]  # 去除邮件头部信息

    # 检查邮件内容中是否包含目标部分
    if "code below: " in email_content:
        code_start_index = email_content.index("code below: ") + len("code below: ")
        code = email_content[code_start_index:]
        print(code)

# 关闭与邮箱服务器的连接
imap_server.logout()
