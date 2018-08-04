# 环境配置

### Mac 基础环境配置

###### 检查组件安装情况
```
brew -v
java -version
git --version
pip -V
```

##### 对应安装方法
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
https://hk.tower.im/projects/99485d41904f43f8b1f62b2e317d6f9b/uploads/bc41acd4074a4992adcd68dc7cbd8562/?version=1
https://hk.tower.im/projects/99485d41904f43f8b1f62b2e317d6f9b/uploads/f249a899cf1f4c568e3a876bd68da5c5/?version=1
easy_install pip
```

### Android SDK 配置

##### 安装
```
下载 https://hk.tower.im/projects/99485d41904f43f8b1f62b2e317d6f9b/uploads/d615287afb62443fa00033dc85c8fb94/?version=1
解压后放到 /usr/local/
前往目录 /usr/local/android-sdk-macosx/tools
启动可执行文件 android 进行安装
```

##### 注意事项
```
需要安装的包如下
Tools
Tools (Preview Channel)
Android 8.0.0 (API 26)
Android 5.1.1 (API 22)
```

### Mac 环境变量配置
```
vi ~/.bash_profile
写入如下内容
    export JAVA_HOME=$(/usr/libexec/java_home)
    export ANDROID_HOME=/usr/local/android-sdk-macosx
    export PATH=${JAVA_HOME}/bin:$PATH
source ~/.bash_profile
```

### appium 配置

##### 安装指定版本 node
```
brew update（可选）
brew install node
sudo npm install n -g
sudo n 8.1.3
```

##### 安装 appium
```
npm install -g appium
npm install wd
```

### 验证上述配置操作是否正确

##### 安装
```
npm install appium-doctor -g
```

##### 验证
```
source ~/.bash_profile
appium-doctor（观察到只有一个警告：［✖ Carthage was NOT found!］）
appium &（观察到输出信息：[Appium] Welcome to Appium）
```

### 修改 chromedriver 版本
```
Mac 下前往目录 /usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac
用（https://hk.tower.im/projects/99485d41904f43f8b1f62b2e317d6f9b/uploads/83b4e119a5204a359b8a5178f1315f60/?version=1）解压后的 chromedriver 代替原来的 chromedriver
```

# 使用
```
source ~/.bash_profile
appium-doctor
appium &
cd PATH/uiauto
pip install -r requirements.txt（只需安装一次）
python startup_xxx.py
```

# 目录结构
```
uiauto
├── README.md
├── __init__.py
├── checker                         # 校验器
│   ├── __init__.py
│   └── check_booking_flow.py       # 校验模块(对应一个业务流程模块)
├── config.py                       # 全局配置
├── core                            # 封装 chromedriver 和 appium
│   ├── __init__.py
│   └── driver.py
├── db                              # 封装 psycopg2
│   ├── __init__.py
│   └── manager.py
├── flow                            # 业务流程
│   ├── __init__.py
│   ├── mini                        # 小程序业务流程
│   │   └── __init__.py
│   └── public                      # 公众号业务流程
│       ├── __init__.py
│       ├── flow_booking.py         # 独立空间业务流程模块(对应一个校验模块)
│       ├── flow_quickoffice.py
│       └── flow_userinfo.py
├── requirements.txt                # Python 依赖
├── startup_mini.py                 # 小程序测试入口
└── startup_public.py               # 公众号测试入口
```
