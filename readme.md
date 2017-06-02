# 羽毛球视频动作片段标注软件


## 软件说明
该软件用于标注羽毛球运动视频中某些特定技术动作片段。支持的技术动作有：
- GYQ(高远球) 
- SQ(杀球) 
- PC(平抽) 
- PD(平挡) 
- TQ(挑球) 
- CQ(搓球) 
- Other(其它)

标注的结果将以**添加**的方式，添加到与所播放视频同一目录底下的`result.txt`文件中，标注的格式为：

```
[视频文件名]\t[起始帧号],[结束帧号]:[动作名]\t[起始帧号],[结束帧号]:[动作名]\t[起始帧号],[结束帧号]:[动作名]……
```
例子：
```
110/05454 1,36:GYQ
110/05455 1,43:GYQ 44,88:PD 89,129:PD 130,181:CQ
110/05458 1,31:GYQ 32,58:CQ 59,82:PD 83,124:GYQ 125,150:SQ
……
```

## 可执行文件下载

这里提供了 Windows 10 系统下编译的可执行文件下载地址。

[action_marking_v0.1.0](http://pan.baidu.com/s/1kVwqyP5)

不需要任何环境配置和依赖安装，可直接运行，使用方法请参考《羽毛球视频动作片段标注软件使用说明》。

## 依赖项

本次开发在 Windows 10 系统中进行。所使用的 Python 版本为 3.5.3 ，开发过程中使用到的其它依赖项有：

- pyqt 5.8.0
- OpenCV 3.2.0

> 温馨提示：为了避免出现全局环境中软件包之间依赖的冲突，建议在 `virtualenv` 创建的虚拟环境中安装各个依赖项。

### pyqt

安装 pyqt5 ：

```bash
$pip install pyqt5
```

### OpenCV

#### Windows 安装

从 opencv 3.x 开始，opencv 其实就已经可以支持 python 3 了，但是官方给出的编译版本还只支持 python 2.7 ，所以如果想要给 python 3 安装 opencv 模块，我们就得自己编译源码，但是这个过程相对繁琐，还容易出错。

这里提供一个非官方的下载地址：

[http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv](http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv)

该网站提供了众多在 windows 平台下的第三方已编译 python 包扩展下载。

进入网页，选择一个合适自己的版本 `opencv_python-xxx.whl` 下载。

比如，我使用 python 3.5 ，所以选择下载 ：

`opencv_python-3.1.0+contrib_opencl-cp35-cp35m-win_amd64.whl` 

`amd64` 适用所有 `64-bit` 的操作系统。

下载好之后，使用 CMD 进入 `.whl` 文件所在目录，执行（以 `opencv_python-3.1.0+contrib_opencl-cp35-cp35m-win_amd64.whl` 为例）：

`pip install opencv_python-3.1.0+contrib_opencl-cp35-cp35m-win_amd64.whl` 

进行安装。

> 如果你想要自己编译安装，可以参考这篇：
> [http://docs.opencv.org/3.1.0/d5/de5/tutorial_py_setup_in_windows.html](http://docs.opencv.org/3.1.0/d5/de5/tutorial_py_setup_in_windows.html)

#### Linux 安装

在 Linux 中要想配置 Python3 可用的 OpenCV 就需要自行编译。编译安装过程如下。

为了便于环境管理，以及避免日后软件包之间的冲突所以我选择在 virtualenv 创建独立的虚拟环境中安装 OpenCV 。

```bash
# 创建环境
$ virtualenv cv_venv
# 启动环境
$ source cv_venv/bin/activate
```

> 注意：为了让 OpenCV 在配置编译项目的过程中能将虚拟环境的 Python 解析器作为编译路径，必须在虚拟环境中进行配置以及编译操作。

其次进入 [OpenCV 官网](http://opencv.org/)下载合适版本的文件，出于稳定性考虑我下载的是已经正式发布的最新版本 OpenCV for Linux VERSION 3.2 。但是如果你想尝试最新的功能可以直接从 OpenCV 的 git 仓库上下载，仓库地址是 `https://github.com/Itseez/opencv.git`

安装附加依赖项。

```bash
# 更新系统包信息并升级已有包
$ sudo apt-get install update
$ sudo apt-get install upgrade

# 安装编译所必须的包
$ sudo apt-get install build-essential

# 安装一些工具，比如 cmake、git等
$ sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

# 安装编解码支持包以及 Python 开发环境
$ sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```

下载之后获得压缩包 `opencv-3.2.0.zip` 。

```bash
$ unzip opencv-3.2.0.zip
```

进入刚解压缩所得文件夹并创建 `build` 文件夹。

```bash
$ cd opencv-3.2.0 && mkdir build
$ cd build
(cv_venv)$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=OFF \
	-D BUILD_opencv_dnn=OFF \
	-D BUILD_EXAMPLES=OFF ..
```

这里对编译时的一些信息进行了配置，比如 cmake 安装路径的前缀、是否安装 c 程序样例等。

其中需要注意的一项是，我将 `BUILD_opencv_dnn` 选项设置为 `OFF` ，这样在生成编译信息的过程中就不会下载 `protobuf-cpp-3.1.0.tar.gz` 文件。因为我在下载 `protobuf-cpp-3.1.0.tar.gz` 文件的过程中一直发生超时错误，目测可能是与天朝网络有关，不过好在 `dnn` 主要用于支持 caffe ，并不影响我正常的使用。

> Tips：如果在执行 cmake 执行过程中遇到 `Failed to download v3.1.0/protobuf-cpp-3.1.0.tar.gz. Status=28;"Timeout was reached"` 的问题可以依上所述将 `dnn` 设置为 OFF，并且可以关注这个 issue [#4690](https://github.com/Homebrew/homebrew-science/issues/4690)。

然后回车执行 cmake ，另外还要注意下输出的 Python 信息是否正确。

```bash 
Python 3:
  Interpreter:     /home/gg/cv_venv/bin/python3.5 (ver 3.5.2)
  Libraries:       /usr/lib/x86_64-linux-gnu/libpython3.5m.so (ver 3.5.2+)
  numpy:           /home/gg/cv_venv/lib/python3.5/site-packages/numpy/core/include
  packages path:   lib/python3.5/site-packages
```

主要看下 `Interpreter` 以及`Python(for build)`这两个选项是否正确，如果不正确那就需要重新配置，有可能是忘了启动虚拟环境，或者另一种解决方案是在 cmake 传参中手动指定 Python3 的路径。

> 其它可选参数：
> `PYTHON(3)_EXECUTABLE` 设定用于执行编译的 python 解释器。
> `PYTHON(3)_NUMPY_INCLUDE_DIRS` 设定 numpy 库的路径。
> 另外还有更多的可选参数，请参见：http://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html

cmake 正确之后，就是长路漫漫的编译。

```bash
$ make -j4
```

`j4` 指定了采用 4 进程编译。

漫长的编译完成后就是安装。

```bash
$ sudo make install
```

安装完成之后在 `/usr/local/lib/python3.5/site-packages/` 路径下就生成了文件 `cv2.cpython-35m-x86_64-linux-gnu.so` ，还需要把文件链接到虚拟环境中去。

```bash
$ cd ~/cv_venv/lib/python3.5/site-packages/
$ ln -s /usr/local/lib/python3.5/site-packages/cv2.cpython-35m-x86_64-linux-gnu.so cv2.so
```

## 运行

```bash
$ python main.py
```

## 其它

- 关于软件使用的更多细节，请参考《羽毛球视频动作片段标注软件使用说明》。
- 关于软件开发过程中更多细节，请参考《羽毛球视频动作片段标注软件开发杂记》

## 关于作者

姓名：叶俊贤
E-mail：yjx.underworld@gmail.com
github：https://github.com/un-knight
个人博客（简书）：http://www.jianshu.com/u/61a39218bfad
雷锋网专栏：https://www.leiphone.com/author/gebiwangda9402
