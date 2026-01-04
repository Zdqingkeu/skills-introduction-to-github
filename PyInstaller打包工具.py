import tkinter as tk
from tkinter import filedialog, messagebox
import PyInstaller.__main__

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PyInstaller打包工具")
        
        self.label = tk.Label(self.root, text="请选择要打包的Python脚本文件：")
        self.label.pack(pady=10)
        
        self.filepath = tk.StringVar()
        self.btn_browse = tk.Button(self.root, text="浏览", command=self.browse_file)
        self.btn_browse.pack(pady=10)
        
        self.label_params = tk.Label(self.root, text="请选择打包参数：")
        self.label_params.pack(pady=10)
        
        self.var_onefile = tk.BooleanVar()
        self.check_onefile = tk.Checkbutton(self.root, text="--onefile", variable=self.var_onefile)
        self.check_onefile.pack()
        
        self.var_noconsole = tk.BooleanVar()
        self.check_noconsole = tk.Checkbutton(self.root, text="--noconsole", variable=self.var_noconsole)
        self.check_noconsole.pack()
        
        self.var_icon = tk.StringVar()
        self.label_icon = tk.Label(self.root, text="图标文件路径：")
        self.label_icon.pack()
        self.entry_icon = tk.Entry(self.root, textvariable=self.var_icon)
        self.entry_icon.pack(pady=10)
        
        self.btn_pack = tk.Button(self.root, text="开始打包", command=self.pack)
        self.btn_pack.pack(pady=10)
    
    def browse_file(self):
        filepath = filedialog.askopenfilename(initialdir="./", title="选择Python脚本文件", filetypes=(("Python files", "*.py"), ("all files", "*.*")))
        self.filepath.set(filepath)
    
    def pack(self):
        filepath = self.filepath.get()
        if not filepath:
            messagebox.showerror("错误", "请先选择要打包的Python脚本文件！")
            return
        
        params = []
        
        if self.var_onefile.get():
            params.append("--onefile")
        
        if self.var_noconsole.get():
            params.append("--noconsole")
        
        icon_path = self.var_icon.get()
        if icon_path:
            params.append(f"--icon={icon_path}")
        
        params.append(filepath)

        PyInstaller.__main__.run(params)
        messagebox.showinfo("提示", "打包完成！")
        

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()

