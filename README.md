# mypkg
ロボットシステム学の講義で作成したROSを用いたpythonのプログラムです。  

# 内容  
このプログラムは、ロボットシステム学の講義で上田先生が作成したコードを一部変更を加えたものです。プログラムを実行すると1秒間隔で数字をカウントして、表示してくれます。
プログラムはcount.py,fivetimes.py,two.pyの三種類です。それぞれ異なる動作をします

# 必要なもの
Raspberry Pi 4 Model B  
os:Ubuntu 20.04.1 LTS  
ROS環境  
ROS Noetic  
ROS Distribution : Noetic Ninjemys

# 前準備  
ラズパイにログインして、以下のことを行います  
$ cd ~/catkin_ws  
$ catkin_make  

# 実行
前準備のコマンドを打ち終わったら以下のコマンドを実行します。複数の端末を用意します。私は三つの端末を使いました
まず端末1で以下のコマンドを実行します。  
$ roscore &  

次にプログラムを実行します。  
1,count.py    
端末1で実行  
$ cd ~/catkin_ws/src/mypkg/scripts  
$ rosrun mypkg count.py  
何も表示されなくて大丈夫  

端末2で実行  
$ rostopic echo /count_up  

端末1と端末2でコマンドを実行することで、端末2に1秒間に1づつカウントしていく様子が表示されます。  

2,two.py  
端末１で実行するものは1のcount.pyと同じなので実行してください。  
端末2で実行  
$ cd ~/catkin_ws/src/mypkg/scripts  
$ rosrun mypkg two.py  
何も表示されなくて大丈夫  

端末3で実行  
$ rostopic echo /two  

端末1と端末2と端末3でコマンドを実行することで、端末1の情報を受け取って、端末3に1秒ごとにcount.pyを2乗した数字が表示されます。  

3,fivetimes.py
2のtwo.pyと同様、端末1で実行してください。 
端末2で実行  
$ cd ~/catkin_ws/src/mypkg/scripts  
$ rosrun mypkg fivetimes.py
何も表示されなくて大丈夫  

端末3で実行
$ rostopic echo /fivetimes  
端末1と端末2と端末3でコマンドを実行することで、端末1の情報を受け取って、端末3に1秒ごとにcount.pyを5倍した数字が表示されます。  

# 動画
youtubeに動画を上げてあります  

# ライセンス
[BSD 3-Clause "New" or "Revised" License](https://github.com/toshiya2771/mypkg/blob/main/LICENSE)








