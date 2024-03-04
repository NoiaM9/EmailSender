import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Sender App")

        self.setup_gui()

    def setup_gui(self):
        # Sender Email
        self.sender_label = tk.Label(self.root, text="Your Email:")
        self.sender_entry = tk.Entry(self.root, width=30)
        self.sender_label.grid(row=0, column=0, padx=10, pady=10)
        self.sender_entry.grid(row=0, column=1, padx=10, pady=10)

        # Sender Password
        self.password_label = tk.Label(self.root, text="Your Password:")
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Receiver Email
        self.receiver_label = tk.Label(self.root, text="Recipient Email:")
        self.receiver_entry = tk.Entry(self.root, width=30)
        self.receiver_label.grid(row=2, column=0, padx=10, pady=10)
        self.receiver_entry.grid(row=2, column=1, padx=10, pady=10)

        # Email Subject
        self.subject_label = tk.Label(self.root, text="Subject:")
        self.subject_entry = tk.Entry(self.root, width=30)
        self.subject_label.grid(row=3, column=0, padx=10, pady=10)
        self.subject_entry.grid(row=3, column=1, padx=10, pady=10)

        # Email Body
        self.body_label = tk.Label(self.root, text="Email Body:")
        self.body_text = tk.Text(self.root, width=30, height=5)
        self.body_label.grid(row=4, column=0, padx=10, pady=10)
        self.body_text.grid(row=4, column=1, padx=10, pady=10)

        # Send Button
        self.send_button = tk.Button(self.root, text="Send Email", command=self.send_email)
        self.send_button.grid(row=5, column=0, columnspan=2, pady=10)

    def send_email(self):
        sender_email = self.sender_entry.get()
        password = self.password_entry.get()
        receiver_email = self.receiver_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", "end-1c")

        try:
            # Set up the MIME
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject

            # Attach body to the email
            message.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server (for Gmail)
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())

            messagebox.showinfo("Success", "Email sent successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSenderApp(root)
    root.mainloop()

