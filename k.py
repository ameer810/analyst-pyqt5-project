# # import smtplib
# # from email.mime.text import MIMEText
# # from email.mime.multipart import MIMEMultipart
# #
# # email = "ameersaad810@gmail.com" # the email where you sent the email
# # password = "aahmpredtiddvxlo"
# # send_to_email = "ameersaad810@gmail.com" # for whom
# # subject = "its me"
# # message = "This is a test email sent by Python. Isn't that cool?!"
# # msg = MIMEMultipart()
# # msg["From"] = email
# # msg["To"] = send_to_email
# # msg["Subject"] = subject
# #
# # msg.attach(MIMEText(message, 'plain'))
# #
# # server = smtplib.SMTP("smtp.gmail.com", 587)
# # server.starttls()
# # server.login(email, password)
# # text = msg.as_string()
# # server.sendmail(email, send_to_email, text)
# # server.quit()
# # print('ok')
# # import requests
# # #a=requests.post('https://ameersaad810.pythonanywhere.com/contact-us/api',{"place": 'jf',"phone_number": 3,"email": 'a@g.com',"content": 'kde',"time":'2021-03-16 16:27:30' })
# # #print('ok')
# # a=requests.get('https://ameersaad810.pythonanywhere.com/contact-us/').json()
# # print(a)
# from selenium import webdriver
# import time
# import pyautogui
# # pyautogui.mouseInfo()
# pyautogui.click(1162,1)
# time.sleep(2)
# pyautogui.doubleClick(50,580)
# time.sleep(2)
# pyautogui.doubleClick(334,20)
# time.sleep(2)
# pyautogui.hotkey('g')
# time.sleep(2)
# pyautogui.hotkey('enter')
# from win32com import client
# import time
#
# word = client.Dispatch("Word.Application")
#
# word.Documents.Open(r'F:\برنامج التحليلات\word\bio latest17.docx')
# # # word.Application.ActivePrinter = "PostScript"
# # word.ActiveDocument.PrintOut()
# # time.sleep(2)
# # word.ActiveDocument.Close()
'''
/ *
ABOUT
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
version
2.05
QT
theme(stylesheet)
specially
developed
for FreeCAD(http: //
    www.freecadweb.org /).
It
might
work
with other software that uses QT styling.

LICENSE
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
Copyright(c)
2016
Pablo
Gil
Fernández

This
work is licensed
under
the
Creative
Commons
Attribution - ShareAlike
4.0
International
License.
To
view
a
copy
of
this
license, visit
http: // creativecommons.org / licenses / by - sa / 4.0 /.

INSTALLATION
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
1) Place
the.qss
files and / images / folder in the
path
that
fits
your
OS:
OSX = / Users / [YOUR_USER_NAME] / Library / Preferences / FreeCAD / Gui / Stylesheets /
        WINDOWS = C: / [INSTALLATION_PATH] / FreeCAD / data / Gui / Stylesheets /
                       LINUX = / home / [YOUR_USER_NAME] /.FreeCAD / Gui / Stylesheets /

                                                           2) In
order
to
display
correctly
images:
2.1) FreeCAD
0.16(development
builds
newer
than
commit
5
b3d50a): that
's it, you are done!

2.2) FreeCAD
0.15: Images
used in the
theme
need
ABSOLUTE
paths
to
be
found
by
FreeCAD, so
you
should
search
the
string
"qss:images"(without
"") and replace
with the real path of your computer.It should be done with all the.qss files you want to install-use
find = qss:images
replace = / Users / myName / Library / Preferences / FreeCAD / Gui / Stylesheets / images

CUSTOMIZATION
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
If
you
would
like
to
change
the
overall
look / style
of
the
theme, just
find and replace
following
colors in the
whole
file:
BACKGROUND(darker
to
ligher)
black
# 505050
# 6e6e6e
# 828282
# a2a2a0
# b6b6b6
# c8c8c8
# c3c3c3
# d2d2d2
# dcdcdc
# e0e0e0
# e6e6e6
# f0f0f0
# f5f5f5 = main background color
white

SELECTION(darker
to
lighter)
# 1b3774
# 2053c0
# 3874f2
# 5e90fa = main selection color
# 6f9efa = used to build QSpinBox up and down buttons, it's used as color in the middle
# 7cabf9
# adc5ed
# cbd8e6


KNOWN
BUGS and TO
DO
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
- please, follow
the
link
to
get
updated
information: http: // forum.freecadweb.org / viewtopic.php?f = 10 & t = 12417
                                                                        * /

                                                                        / *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Reset
elements
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
/ *Reseting
everything
helps
to
unify
styles
across
different
operating
systems * /
* {
    padding: 0px;
margin: 0
px;
border: 0
px;
border - style: none;
border - image: none;
outline: 0;
}

/ *specific
reset
for elements inside QToolBar * /
QToolBar * {
margin: 0
px;
padding: 0
px;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Main
window
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QMainWindow,
QDialog,
QDockWidget,
QToolBar
{
    background - color:  # f5f5f5; /* main background color */
}

QMdiArea
{
    background - image: url(qss: images / background_freecad.png);
background - position: center
center;
background - repeat: no - repeat;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
MENUS
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QMenuBar,
QMenuBar::item
{
    color: black;
background - color:  # f5f5f5; /* main background color */
}

QMenu,
QMenu::item
{
    color: black;
background - color:  # f5f5f5; /* main background color */
text - decoration: none;
}

QMenuBar::item: selected,
QMenuBar::item: pressed,
QMenu::item: selected,
QMenu::item: pressed
{
    color: white;
background - color:  # 5e90fa;
}

QMenu::right - arrow
{
    width: 10px;
height: 10
px;
image: url(qss:images / right_arrow_dark.png);
margin - right: 2
px;
}

QMenu::right - arrow: selected
{
    image: url(qss: images / right_arrow_lighter.png);
}

QMenu::item
{
    padding: 2px 16px 2px 26px; / *make
room
for icon at left * /
border: 1
px
solid
transparent; / *reserve
space
for selection border * /
}

QMenu::
    icon
{
    margin - left: 2px;
}

QMenu::separator
{
    height: 1px;
background - color: rgba(0, 0, 0, 30);
margin: 6
px
4
px;
}

QMenu::indicator: non - exclusive:checked
{
    color: white;
}

/ *Fix
for elements inside a drop-down menu * /
QMenu QRadioButton,
QMenu QCheckBox,
QMenu QPushButton,
QMenu QToolButton {
color: black; /
*same as regular
QRadioButton and QCheckBox * /
}

QMenu
QRadioButton: hover,
QMenu
QCheckBox: hover,
QMenu
QPushButton: hover,
QMenu
QToolButton: hover,
QMenu
QPushButton: pressed,
QMenu
QToolButton: pressed,
QMenu
QPushButton: selected,
QMenu
QToolButton: selected
{
    color: white;
background - color:  # 5e90fa; /* same as QMenu::item:selected and QMenu::item:pressed */
}

QMenu
QRadioButton: disabled,
QMenu
QCheckBox: disabled
{
    color:  # 6e6e6e;
}

QMenu
QRadioButton::indicator: disabled,
QMenu
QCheckBox::indicator: disabled
{
    color:  # 6e6e6e;
        background - color: transparent;
border: 1
px
solid  # 6e6e6e;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tool
bar
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QToolBar
{
    border: none;
padding: 2
px;
}

QToolBar::handle: top,
QToolBar::handle: bottom,
QToolBar::handle: horizontal
{
    background - image: url(qss: images / Hmovetoolbar_dark.png);
width: 10
px;
margin: 4
px
2
px;
background - position: top
right;
background - repeat: repeat - y;
}

QToolBar::handle: left,
QToolBar::handle: right,
QToolBar::handle: vertical
{
    background - image: url(qss: images / Vmovetoolbar_dark.png);
height: 10
px;
margin: 2
px
4
px;
background - position: left
bottom;
background - repeat: repeat - x;
}

QToolBar::separator: top,
QToolBar::separator: bottom,
QToolBar::separator: horizontal
{
    width: 1px;
margin: 6
px
4
px;
background - color: rgba(0, 0, 0, 30);
}

QToolBar::separator: left,
QToolBar::separator: right,
QToolBar::separator: vertical
{
    height: 1px;
margin: 4
px
6
px;
background - color: rgba(0, 0, 0, 30);
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Group
box
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QGroupBox
{
    color: rgba(0, 0, 0, 120);
border: 1
px
solid
rgba(0, 0, 0, 20); / *lighter
than
its
own
border - color * /;
border - radius: 3
px;
margin - top: 10
px;
padding: 6
px;
background - color: rgba(255, 255, 255, 15);
}

QGroupBox: title
{
    top: -8px;
left: 12
px;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tooltip
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QToolTip
{
    color: white;
background - color:  # 828282;
/ *opacity: 90 %;
doesn
't correctly work */
padding: 4
px;
border - radius: 3
px; / *has
no
effect * /
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Dock
widget
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QDockWidget
{
    color: rgba(0, 0, 0, 120);
titlebar - close - icon: url(qss:images / close_dark.png);
titlebar - normal - icon: url(qss:images / undock_dark.png);
}

QDockWidget::title
{
    text - align: center;
background - color: rgba(0, 0, 0, 10);
border: 4
px
solid  # f5f5f5; /* fix to simulate margin between this :title and tabs */ /* same as main background color */
border - radius: 6
px; / *bigger
than
normal
due
to
previous
border
fix * /
padding: 4
px
0
px; / *also
needed
because
of
previous
border
fix * /
}

QDockWidget::close - button,
             QDockWidget::float - button
{
    border: none;
background: transparent;
border - radius: 3
px;
subcontrol - origin: padding;
subcontrol - position: right
center;
}

QDockWidget::close - button
{
    right: 4px;
}

QDockWidget::float - button
{
    right: 22px;
}

QDockWidget::close - button: hover,
QDockWidget::float - button: hover
{
    background - color: rgba(0, 0, 0, 15);
}

QDockWidget::close - button: pressed,
QDockWidget::float - button: pressed
{
    background - color: rgba(0, 0, 0, 30);
}

/ *fix
for Python Console(probably there is a smarter way to arrive to it) * /
QDockWidget > QFrame {
background-color:  # f0f0f0;
    border: 1
px
solid  # c3c3c3;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Progress
bar
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QProgressBar,
QProgressBar: horizontal
{
    color: white;
background - color: rgba(0, 0, 0, 10);
text - align: center;
border: 1
px
solid
rgba(0, 0, 0, 80);
padding: 1
px;
border - radius: 3
px;
}
QProgressBar::chunk,
              QProgressBar::chunk: horizontal
{
    background - color: qlineargradient(spread: pad, x1: 1, y1: 0.545, x2: 1, y2: 0, stop: 0  # 3874f2, stop:1 #5e90fa);
border - radius: 3
px;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Scroll
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QAbstractScrollArea
{
    border - radius: 2px;
background - color: transparent;
}

QAbstractScrollArea::corner
{
    border: none;
background - color: transparent;
}

QScrollBar: horizontal
{
    background - color: transparent;
height: 15
px;
margin: 0
px;
}

QScrollBar::handle: vertical,
QScrollBar::handle: horizontal
{
    background - color: rgba(0, 0, 0, 80);
}

QScrollBar::handle: vertical:hover,
                             QScrollBar::handle: horizontal:hover
{
    background - color: rgba(0, 0, 0, 100);
}

QScrollBar::handle: horizontal
{
    min - width: 5px;
border - radius: 3
px;
margin: 4
px
15
px;
}

QScrollBar::sub - line: horizontal
{
    margin: 1px 3px 0px 3px; / *1
px
to
correctly
fit
the
10
px
width
image * /
border - image: url(qss:images / left_arrow_dark.png);
width: 6
px;
height: 10
px;
subcontrol - position: left;
subcontrol - origin: margin;
}

QScrollBar::add - line: horizontal
{
    margin: 1px 3px 0px 3px; / *1
px
to
correctly
fit
the
10
px
width
image * /
border - image: url(qss:images / right_arrow_dark.png);
width: 6
px;
height: 10
px;
subcontrol - position: right;
subcontrol - origin: margin;
}

QScrollBar::sub - line: horizontal:hover,
                                   QScrollBar::sub - line: horizontal:on
{
    border - image: url(qss: images / left_arrow_darker.png);
}

QScrollBar::add - line: horizontal:hover,
                                   QScrollBar::add - line: horizontal:on
{
    border - image: url(qss: images / right_arrow_darker.png);
}

QScrollBar::up - arrow: horizontal,
QScrollBar::down - arrow: horizontal
{
    background - color: none;
}

QScrollBar::add - page: horizontal,
QScrollBar::sub - page: horizontal
{
    background - color: transparent;
}

QScrollBar: vertical
{
    background - color: transparent;
width: 15
px;
margin: 0
px;
}

QScrollBar::handle: vertical
{
    min - height: 5px;
border - radius: 3
px;
margin: 15
px
4
px;
}

QScrollBar::sub - line: vertical
{
    margin: 3px 0px 3px 1px; / *1
px
to
correctly
fit
the
10
px
width
image * /
border - image: url(qss:images / up_arrow_dark.png);
height: 6
px;
width: 10
px;
subcontrol - position: top;
subcontrol - origin: margin;
}

QScrollBar::add - line: vertical
{
    margin: 3px 0px 3px 1px; / *1
px
to
correctly
fit
the
10
px
width
image * /
border - image: url(qss:images / down_arrow_dark.png);
height: 6
px;
width: 10
px;
subcontrol - position: bottom;
subcontrol - origin: margin;
}

QScrollBar::sub - line: vertical:hover,
                                 QScrollBar::sub - line: vertical:on
{
    border - image: url(qss: images / up_arrow_darker.png);
}

QScrollBar::add - line: vertical:hover,
                                 QScrollBar::add - line: vertical:on
{
    border - image: url(qss: images / down_arrow_darker.png);
}

QScrollBar::up - arrow: vertical,
QScrollBar::down - arrow: vertical
{
    background - color: none;
}

QScrollBar::add - page: vertical,
QScrollBar::sub - page: vertical
{
    background - color: transparent;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tab
bar
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QTabWidget::pane
{
    background - color: transparent; / *temporal(transparent
background) * / / *tab
content
background
color * /
position: absolute;
}

QTabWidget::pane: top
{
    top: -1px;
border - top: 1
px
solid  # d2d2d2;
}

QTabWidget::pane: bottom
{
    bottom: -1px;
border - bottom: 1
px
solid  # d2d2d2;
}

QTabWidget::pane: left
{
    right: -1px;
border - right: 1
px
solid  # d2d2d2;
}

QTabWidget::pane: right
{
    left: -1px;
border - left: 1
px
solid  # d2d2d2;
}

QTabWidget::tab - bar: top,
QTabWidget::tab - bar: bottom
{
    left: 10px;
}

QTabWidget::tab - bar: left,
QTabWidget::tab - bar: right
{
    top: 10px;
}

QTabBar
{
    qproperty - drawBase: 0; / *important * /
                                background - color: transparent;
}

/ *Workaround
for QTabBars created from docked QDockWidgets which don't draw the border if not set and reseted as follows: */
QTabBar {
border-top: 1
px
solid  # d2d2d2;  /* set color for all QTabBars */
}
QDockWidget
QTabBar
{
    border - color: transparent; / *set
color
for all QTabBars but ones created from QDockWidget * /
}
QDialog QTabBar {
border-color: transparent; /
    *set
color
for QTabBars inside Preferences dialog * /
}
/ * end fix * /

QTabBar::
    tab
{
    background - color: transparent;
border: 1
px
solid
transparent;
padding: 3
px;
}

QTabBar::tab: top,
QTabBar::tab: bottom
{
    border - top - width: 4px; / *same as selected
tab
colored
border in order
to
center
close - button * /
border - bottom - width: 4
px; / *same as selected
tab
colored
border in order
to
center
close - button * /
min - width: 11
ex;
margin - left: 2
px;
margin - right: 2
px;
}

QTabBar::tab: left,
QTabBar::tab: right
{
    border - left - width: 4px; / *same as selected
tab
colored
border in order
to
center
close - button * /
border - right - width: 4
px; / *same as selected
tab
colored
border in order
to
center
close - button * /
min - height: 14
ex;
margin - top: 2
px;
margin - bottom: 2
px;
}

QTabBar::tab: selected
{
    background - color:  # f5f5f5; /* same as tab content background color */
        border - color:  # d2d2d2;
}

QTabBar::tab: top:selected
{
    border - top: 4px solid qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0
    # 5e90fa, stop:1 #3874f2); /* selection color */
    border - bottom - color:  # f5f5f5; /* same as tab content background color */
}

QTabBar::tab: bottom:selected
{
    border - bottom: 4px solid qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1,
    stop: 0  # 5e90fa, stop:1 #3874f2); /* selection color */
border - top - color:  # f5f5f5; /* same as tab content background color */
}

QTabBar::tab: right:selected
{
border - left: 4
px
solid
qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0  # 5e90fa, stop:1 #3874f2); /* selection color */
border - right - color:  # f5f5f5; /* same as tab content background color */
}

QTabBar::tab: left:selected
{
    border - right: 4px solid qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0
    # 5e90fa, stop:1 #3874f2); /* selection color */
    border - left - color:  # f5f5f5; /* same as tab content background color */
}

QTabBar::tab:!selected
{
    color: rgba(0, 0, 0, 160);
}

QTabBar::tab:!selected: hover
{
    color: rgba(0, 0, 0, 220);
background - color: rgba(0, 0, 0, 20);
}

QTabBar::tab: first:selected
{
    margin - left: 0; / *the
first
selected
tab
has
nothing
to
overlap
with on the left * /
}

QTabBar::
    tab: last:selected
{
    margin - right: 0; / *the
last
selected
tab
has
nothing
to
overlap
with on the right * /
}

QTabBar::
    tab: only - one
{
    margin: 0; / * if there is only
one
tab, we
don
't want overlapping margins */
}

/ *hack
to
access
Preference
TabBar
background * /
QDialog
# Gui__Dialog__DlgPreferences > QFrame QFrame {
background - color: transparent; / *main
background
color( in Windows is  # f5f5f5) */
}

/ *fix
for previous hack that broke QTabWidget background on Windows * /
QDialog  # Gui__Dialog__DlgPreferences QTabWidget::pane {
background-color: transparent; /
    *temporal(transparent
background) * /
}

/ *hack
to
correctly
align
Preferences
icon
list
on
OSX * /
QDialog  # Gui__Dialog__DlgPreferences > QListView {
min - width: 130
px;
}

/ *unique
styles
for sections inside Preferences * /
QDialog  # Gui__Dialog__DlgPreferences > QListView::item {
border-radius: 6
px;
}

QDialog
# Gui__Dialog__DlgPreferences > QListView::item:hover {
background - color:  # dcdcdc;
}

QDialog
# Gui__Dialog__DlgPreferences > QListView::item:selected {
color: white;
background - color:  # 5e90fa;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tab
bar
buttons
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
/ *Close
button * /
QTabBar::close - button
{
    subcontrol - origin: margin;
subcontrol - position: center
right; / *only
works
for QT 4.6 and newer * /;
border-radius: 2
px;
background - image: url(qss:images / close_dark.png);
background - position: center
center;
background - repeat: none;
}

QTabBar::close - button: hover
{
    background - color: rgba(0, 0, 0, 20);
}

QTabBar::close - button: pressed
{
    background - color: rgba(0, 0, 0, 30);
}

/ *Fix
for lists inside Model tab * /
QDockWidget QTreeView,
QDockWidget QListView,
QDockWidget QTableView {
margin: 6
px;
border: 1
px
solid  # c3c3c3; /* same as regular QTreeView, QListView and QTableView */
min - height: 40
px; / *neccesary in some
areas
of
FreeCAD * /
}

/ *Buttons
to
scroll
tabs if there is not space
to
show
all
of
them: * /
QTabBar::scroller
{
    width: 20px; / *the
width
of
the
scroll
buttons * /
}

QTabBar
QToolButton,
QTabBar
QToolButton: hover
{
    background - color:  # f5f5f5; /* same as main background color */
}

QTabBar
QToolButton::right - arrow: enabled
{
    image: url(qss: images / right_arrow_dark.png);
}

QTabBar
QToolButton::right - arrow: disabled,
QTabBar
QToolButton::right - arrow: off
{
    image: url(qss: images / right_arrow_disabled_dark.png);
}

QTabBar
QToolButton::right - arrow: hover
{
    image: url(qss: images / right_arrow_darker.png);
}

QTabBar
QToolButton::left - arrow: enabled
{
    image: url(qss: images / left_arrow_dark.png);
}

QTabBar
QToolButton::left - arrow: disabled,
QTabBar
QToolButton::left - arrow: off
{
    image: url(qss: images / left_arrow_disabled_dark.png);
}

QTabBar
QToolButton::left - arrow: hover
{
    image: url(qss: images / left_arrow_darker.png);
}

QTabBar
QToolButton::up - arrow: enabled
{
    image: url(qss: images / up_arrow_dark.png);
}

QTabBar
QToolButton::up - arrow: disabled,
QTabBar
QToolButton::up - arrow: off
{
    image: url(qss: images / up_arrow_disabled_dark.png);
}

QTabBar
QToolButton::up - arrow: hover
{
    image: url(qss: images / up_arrow_darker.png);
}

QTabBar
QToolButton::down - arrow: enabled
{
    image: url(qss: images / down_arrow_dark.png);
}

QTabBar
QToolButton::down - arrow: disabled,
QTabBar
QToolButton::down - arrow: off
{
    image: url(qss: images / down_arrow_disabled_dark.png);
}

QTabBar
QToolButton::down - arrow: hover
{
    image: url(qss: images / down_arrow_darker.png);
}

QTabBar::tear
{
/ * default
OS
tear
better * /
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tree and list
views
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QTreeView,
QListView,
QTableView
{
    background - color:  # f0f0f0;
        alternate - background - color:  # e6e6e6; /* related with QListView background  */
border: 1
px
solid  # c3c3c3;
selection - color: white;
selection - background - color:  # 5e90fa; /* should be similar to QListView::item selected background-color */
show - decoration - selected: 1; / *make
the
selection
span
the
entire
width
of
the
view * /
border - radius: 3
px;
}

QListView::item: hover,
QTreeView::item: hover
{
    background - color: transparent; / *fix
to
homogenize
it
on
all
OSs * /
}

QListView::item: selected,
QTreeView::item: selected
{
    color: white; / *should
be
similar
to
QListView
selection - color * /
background - color:  # 5e90fa; /* should be similar to QListView selection-background-color */
show - decoration - selected: 1; / *make
the
selection
span
the
entire
width
of
the
view * /
}

/ *Property
Editor
QTreeView(FreeCAD
custom
widget) * /
Gui - -PropertyEditor - -PropertyEditor
{
    gridline - color:  # d2d2d2; /* same as Group header background */
}

/ * fix
for column items background when a link is present * /
Gui--PropertyEditor--PropertyEditor > QWidget > QFrame:focus
{
    background - color:  # cbd8e6; /* same as focused background color */
}

/ * hack
to
hide
weird
redundant
information
inside
the
value
of
a
Placement
cell * /
Gui - -PropertyEditor - -PropertyEditor > QWidget > QWidget > QLabel,
Gui - -PropertyEditor - -PropertyEditor > QWidget > QWidget > QLabel: disabled
{
    color: transparent;
background - color: transparent;
border: none;
border - radius: 0
px;
margin: 0
px;
padding: 0
px;
}

/ *hack
to
hide
non
editable
cells
inside
Property
values * /
Gui - -PropertyEditor - -PropertyEditor
QLineEdit: read - only,
Gui - -PropertyEditor - -PropertyEditor
QLineEdit: disabled,
Gui - -PropertyEditor - -PropertyEditor
QAbstractSpinBox: read - only,
Gui - -PropertyEditor - -PropertyEditor
QAbstractSpinBox: disabled
{
    color: transparent;
border - color: transparent;
background - color: transparent;
selection - color: transparent;
selection - background - color: transparent;
}

/ *hack
to
disable
margin
inside
Property
values
to
following
elements * /
Gui - -PropertyEditor - -PropertyEditor
QSpinBox,
Gui - -PropertyEditor - -PropertyEditor
QDoubleSpinBox,
Gui - -PropertyEditor - -PropertyEditor
QAbstractSpinBox,
Gui - -PropertyEditor - -PropertyEditor
QLineEdit,
Gui - -PropertyEditor - -PropertyEditor
QComboBox
{
    margin - left: 0px;
margin - right: 0
px;
padding - top: 0
px;
padding - bottom: 0
px;
}

/ *reset
min - height
to
0
px
inside
list
views * /
QTreeView > QWidget > QComboBox,
QTreeView > QWidget > QAbstractSpinBox,
QTreeView > QWidget > QSpinBox,
QTreeView > QWidget > QDoubleSpinBox,
QTreeView > QWidget > QLineEdit,
QTreeView > QWidget > QTextEdit,
QTreeView > QWidget > QTimeEdit,
QTreeView > QWidget > QDateEdit,
QTreeView > QWidget > QDateTimeEdit,
QTreeView > QWidget > Gui - -ColorButton
{
    min - height: 0px;
}

/ *set
border - radius
to
0
px
inside
list
views * /
QTreeView > QWidget > QComboBox,
QTreeView > QWidget > QAbstractSpinBox,
QTreeView > QWidget > QSpinBox,
QTreeView > QWidget > QDoubleSpinBox,
QTreeView > QWidget > QLineEdit,
QTreeView > QWidget > QTextEdit,
QTreeView > QWidget > QTimeEdit,
QTreeView > QWidget > QDateEdit,
QTreeView > QWidget > QDateTimeEdit,
QTreeView > QWidget > QComboBox: drop - down,
QTreeView > QWidget > QAbstractSpinBox: up - button,
QTreeView > QWidget > QSpinBox: up - button,
QTreeView > QWidget > QDoubleSpinBox: up - button,
QTreeView > QWidget > QTimeEdit: up - button,
QTreeView > QWidget > QDateEdit: up - button,
QTreeView > QWidget > QDateTimeEdit: up - button,
QTreeView > QWidget > QAbstractSpinBox: down - button,
QTreeView > QWidget > QSpinBox: down - button,
QTreeView > QWidget > QDoubleSpinBox: down - button,
QTreeView > QWidget > QTimeEdit: down - button,
QTreeView > QWidget > QDateEdit: down - button,
QTreeView > QWidget > QDateTimeEdit: down - button,
QTreeView > QWidget > Gui - -ColorButton
{
    border - radius: 0px;
}

/ *set
focus
colors
to
best
viewing
the
editable
fields * /
QTreeView > QWidget > QComboBox: focus,
QTreeView > QWidget > QAbstractSpinBox: focus,
QTreeView > QWidget > QSpinBox: focus,
QTreeView > QWidget > QDoubleSpinBox: focus,
QTreeView > QWidget > QLineEdit: focus,
QTreeView > QWidget > QTextEdit: focus,
QTreeView > QWidget > QTimeEdit: focus,
QTreeView > QWidget > QDateEdit: focus,
QTreeView > QWidget > QDateTimeEdit: focus
{
    border - color:  # cbd8e6; /* same as focused background color */
        border - bottom - color:  # 7cabf9; /* same as focused border color */
}

QTreeView > QWidget > QAbstractSpinBox: read - only,
QTreeView > QWidget > QSpinBox: read - only,
QTreeView > QWidget > QDoubleSpinBox: read - only,
QTreeView > QWidget > QLineEdit: read - only,
QTreeView > QWidget > QTextEdit: read - only,
QTreeView > QWidget > QTimeEdit: read - only,
QTreeView > QWidget > QDateEdit: read - only,
QTreeView > QWidget > QDateTimeEdit: read - only
{
    color: transparent;
background - color: transparent;
border - color: transparent;
}

/ *Fix
to
correctly(not totally)
draw
QTextEdit
on
OSX
at
Page
properties: "Page result", "Template" and "Editable Texts" * /
                           Gui - -PropertyEditor - -PropertyEditor > QWidget > QWidget > QWidget
{
    min - height: 14px;
border - radius: 0
px; / *reset * /
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Header
of
tree and list
views
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QHeaderView
{
    background - color:  # c3c3c3;
        border - top - left - radius: 2
px; / *1
px
less
than
its
container * /
border - top - right - radius: 2
px; / *1
px
less
than
its
container * /
border - bottom - left - radius: 0
px;
border - bottom - right - radius: 0
px;
}

QHeaderView::section
{
    border: none;
padding: 4
px
6
px;
background - color:  # c3c3c3;
}

QHeaderView::section: horizontal
{
    padding: 4px 6px; / *left and right
value
similar
to
QHeaderView::section * /
             border - right: 1
px
solid
rgba(0, 0, 0, 30);
}

QHeaderView::section: vertical
{
    border - bottom: 1px solid rgba(0, 0, 0, 30);
}

QTableCornerButton::section
{
    background - color:  # c3c3c3;
        border - top: none;
border - left: none;
border - right: 1
px
solid
rgba(0, 0, 0, 30);
border - bottom: 1
px
solid
rgba(0, 0, 0, 30);
}

QHeaderView::section: last
{
    border - right: none;
}

QHeaderView::up - arrow
{
    image: url(qss: images / up_arrow_dark.png);
}

QHeaderView::up - arrow: hover
{
    image: url(qss: images / up_arrow_darker.png);
}

QHeaderView::down - arrow
{
    image: url(qss: images / down_arrow_dark.png);
}

QHeaderView::down - arrow: hover
{
    image: url(qss: images / down_arrow_darker.png);
}

/ *Group
header
inside
Property
Editor(FreeCAD
custom
widget) * /
Gui - -PropertyEditor - -PropertyEditor
{
    qproperty - groupTextColor:  # 828282; /* same as main background color */
        qproperty - groupBackground:  # d2d2d2; /* same as item gridlines */
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Branch
system
for QTreeViews
    == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QTreeView::
    branch
{
    background: transparent;
}

QTreeView::branch: has - siblings:!adjoins - item
{
    border - image: url(qss: images / branch_vline.png) 0;
}

QTreeView::branch: has - siblings:adjoins - item
{
    border - image: url(qss: images / branch_more.png) 0;
}

QTreeView::branch:!has - children:!has - siblings: adjoins - item
{
    border - image: url(qss: images / branch_end.png) 0;
}

QTreeView::branch: closed:has - children: has - siblings
{
    image: url(qss: images / branch_closed_dark.png);
}

QTreeView::branch: has - children:!has - siblings: closed
{
    image: url(qss: images / branch_closed_dark.png);
border - image: url(qss:images / branch_end.png) 0;
}

QTreeView::branch: open:has - children: has - siblings
{
    image: url(qss: images / branch_open_dark.png);
border - image: url(qss:images / branch_more.png) 0;
}

QTreeView::branch: open:has - children:!has - siblings
{
    image: url(qss: images / branch_open_dark.png);
border - image: url(qss:images / branch_end.png) 0;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Splitter and windows
separator
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QSplitter::handle
{
    margin: 0px 11px;
padding: 0
px;
}

QSplitter::handle: horizontal
{
    background - image: url(qss: images / splitter_vertical_dark.png);
background - position: center
center;
background - repeat: none;
margin: 4
px
2
px
4
px
2
px;
width: 2
px;
}

QSplitter::handle: vertical
{
    background - image: url(qss: images / splitter_horizontal_dark.png);
background - position: center
center;
background - repeat: none;
margin: 2
px
4
px
2
px
4
px;
height: 2
px;
}

/ *Similar
to
the
splitter is the
following
window
separator(but
horizontal / vertical is on
the
opposite
way) * /
QMainWindow::separator
{
    background - position: center center;
background - repeat: none;
}

QMainWindow::separator: horizontal
{
    height: 2px;
background - image: url(qss:images / splitter_horizontal_dark.png);
margin: 4
px
2
px
4
px
2
px;
}

QMainWindow::separator: vertical
{
    width: 2px;
background - image: url(qss:images / splitter_vertical_dark.png);
margin: 2
px
4
px
2
px
4
px;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Text / Python
editor(macros, etc...)
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QPlainTextEdit,
QPlainTextEdit: focus
{
    background - color:  # f0f0f0;
        selection - color: white;
selection - background - color:  # 3874f2;
border: 1
px
solid  # c3c3c3;
border - radius: 3
px;
margin: 4
px;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tasks
panel(custom
FreeCAD


class )
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
/ * Action group * /
QFrame[class ="panel"] {


background - color: transparent; / *temporal(transparent
background) * /
}

QSint - -ActionGroup
{
padding: 0
px; / * if not reset, it
might
create
problems
with QPushButtons and other elements * /
margin: 0
px; / * if not reset, it
might
create
problems
with QPushButtons and other elements * /
}

/ *Separator
line * /
QSint - -ActionGroup
QFrame[height = "1"],
QSint - -ActionGroup
QFrame[height = "2"],
QSint - -ActionGroup
QFrame[height = "3"],
QSint - -ActionGroup
QFrame[width = "1"],
QSint - -ActionGroup
QFrame[width = "2"],
QSint - -ActionGroup
QFrame[width = "3"] {
border - color: rgba(0, 0, 0, 60);
}

/ *Panel
header * /
QSint - -ActionGroup
QFrame[


class ="header"] {


border: none;
background - color:  # b6b6b6; /* Task Panel Header background color */
border - top - left - radius: 3
px;
border - top - right - radius: 3
px;
border - bottom - left - radius: 0
px;
border - bottom - right - radius: 0
px;
margin: 0
px;
padding: 0
px;
}

QSint - -ActionGroup
QFrame[


class ="header"]:hover


{
background - color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # 5e90fa, stop:1 #3874f2);
}

QSint - -ActionGroup
QToolButton[


class ="header"] {


color: white; / *Task
Panel
Header
text
color * /
text - align: left;
font - weight: bold;
border: none;
margin: 0
px;
padding: 0
px;
}

QSint - -ActionGroup
QFrame[


class ="header"] QLabel {


background - color: transparent;
background - image: url(qss:images / down_arrow_light.png);
background - repeat: none;
background - position: center
center;
padding: 0
px;
margin: 0
px;
}

QSint - -ActionGroup
QFrame[


class ="header"] QLabel:hover


{
background - color: transparent;
background - image: url(qss:images / down_arrow_lighter.png);
}

QSint - -ActionGroup
QFrame[


class ="header"] QLabel[fold="true"] {


background - color: transparent;
background - image: url(qss:images / up_arrow_light.png);
background - repeat: none;
background - position: center
center;
padding: 0
px;
margin: 0
px;
}

QSint - -ActionGroup
QFrame[


class ="header"] QLabel[fold="true"]:hover


{
background - color: transparent;
background - image: url(qss:images / up_arrow_lighter.png);
}

QSint - -ActionGroup
QFrame[


class ="content"] {


background - color:  # e6e6e6; /* Task Panel background color */
margin: 0
px;
padding: 0
px;
border: none;
border - top - left - radius: 0
px;
border - top - right - radius: 0
px;
border - bottom - left - radius: 3
px;
border - bottom - right - radius: 3
px;
}

QSint - -ActionGroup
QFrame[


class ="content"] > QWidget {


background - color:  # e6e6e6; /* Task Panel background color */
}

/ *Fixs
for tabs inside Task Panel * /
QSint--ActionGroup QFrame[class ="content"] QTabBar::
    tab: top:selected
{
border - bottom - color:  # e6e6e6; /* same as Task Panel background color */
}

QSint - -ActionGroup
QFrame[


class ="content"] QTabBar::


    tab: bottom:selected
{
border - top - color:  # e6e6e6; /* same as Task Panel background color */
}

QSint - -ActionGroup
QFrame[


class ="content"] QTabBar::


    tab: right:selected
{
border - right - color:  # e6e6e6; /* same as Task Panel background color */
}

QSint - -ActionGroup
QFrame[


class ="content"] QTabBar::


    tab: left:selected
{
border - left - color:  # e6e6e6; /* same as Task Panel background color */
}

/ *Fix
for buttons with icons that showed cropped (still not happy with result) * /
QSint--ActionGroup QFrame[class ="content"] > QWidget > QPushButton {
padding: 2
px; / *bigger
padding
crops
text and icons... * /
margin: 0
px;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Buttons
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
/ *Common * /
   QComboBox,
  QAbstractSpinBox,
  QSpinBox,
  QDoubleSpinBox,
  QLineEdit,
  QTextEdit,
  QTimeEdit,
  QDateEdit,
  QDateTimeEdit
{
color:  # 6e6e6e;
background - color:  # e0e0e0;
selection - color: white;
selection - background - color:  # 5e90fa;
border: 1
px
solid  # e0e0e0;
border - radius: 3
px;
min - width: 50
px; / *it
ensures
the
default
value is correctly
displayed * /
min - height: 20
px; / *important
to
be
a
pair
number in order
to
up / down
buttons
to
be
divisible
by
two( if not set
could
create
a
blank
line in Ubuntu.Its
downside is that
it
's needed to reset it (min-width: 0px) on following elements that can'
t
have
it
such as fields
inside
QToolBar and inside
QTreeView(Property
editor) * /
padding: 1
px
2
px; / *temporal: could
don
't be compatible with elements inside Tree/List view */
}

/ *shifts
text / number
editable
field
to
the
left
to
make
space
for the up / down or drop - down buttons * /
QComboBox,
QAbstractSpinBox,
QSpinBox,
QDoubleSpinBox,
QTimeEdit,
QDateEdit,
QDateTimeEdit
{
    padding - right: 20px;
}

/ *when
QTextEdit
are
no
editable * /
QTextEdit:!editable
{
    background - color:  # f0f0f0;
        border: 1
px
solid  # c3c3c3;
}

QComboBox: focus,
QAbstractSpinBox: focus,
QSpinBox: focus,
QDoubleSpinBox: focus,
QLineEdit: focus,
QTextEdit: focus,
QTimeEdit: focus,
QDateEdit: focus,
QDateTimeEdit: focus
{
    color: black;
border - color:  # 7cabf9;
border - right - color: qlineargradient(
    spread: pad, x1: 1, y1: 0.8, x2: 1, y2: 0, stop: 0  # 5e90fa, stop:1 #7cabf9); /* same as up/down or drop-down button color */
background - color:  # cbd8e6;
}

QComboBox: disabled,
QAbstractSpinBox: disabled,
QSpinBox: disabled,
QDoubleSpinBox: disabled,
QLineEdit: disabled,
QTextEdit: disabled,
QTimeEdit: disabled,
QDateEdit: disabled,
QDateTimeEdit: disabled
{
    color:  #000000;
        background - color:  # e0e0e0; /* same as enabled color */
border - color:  # e0e0e0; /* same as enabled color */
}

QAbstractSpinBox: up - button,
QSpinBox: up - button,
QDoubleSpinBox: up - button,
QTimeEdit: up - button,
QDateEdit: up - button,
QDateTimeEdit: up - button,
QAbstractSpinBox: down - button,
QSpinBox: down - button,
QDoubleSpinBox: down - button,
QTimeEdit: down - button,
QDateEdit: down - button,
QDateTimeEdit: down - button
{
    background - color:  # d2d2d2;
        subcontrol - origin: border; / *important * /
                                        width: 20
px; / *same as QComboBox...QDateTimeEdit
padding - right * /
}

QAbstractSpinBox: up - button,
QSpinBox: up - button,
QDoubleSpinBox: up - button,
QTimeEdit: up - button,
QDateEdit: up - button,
QDateTimeEdit: up - button
{
    subcontrol - position: top right;
border - top - right - radius: 3
px;
}

QAbstractSpinBox: down - button,
QSpinBox: down - button,
QDoubleSpinBox: down - button,
QTimeEdit: down - button,
QDateEdit: down - button,
QDateTimeEdit: down - button
{
    subcontrol - position: bottom right;
border - bottom - right - radius: 3
px;
}

QAbstractSpinBox: up - button:focus,
                              QSpinBox: up - button:focus,
                                                    QDoubleSpinBox: up - button:focus,
                                                                                QTimeEdit: up - button:focus,
                                                                                                       QDateEdit: up - button:focus,
                                                                                                                              QDateTimeEdit: up - button:focus
{
    background - color: qlineargradient(spread: pad, x1: 1, y1: 0.8, x2: 1, y2: 0, stop: 0  # 6f9efa, stop:1 #7cabf9);
}

QAbstractSpinBox: down - button:focus,
                                QSpinBox: down - button:focus,
                                                        QDoubleSpinBox: down - button:focus,
                                                                                      QTimeEdit: down - button:focus,
                                                                                                               QDateEdit: down - button:focus,
                                                                                                                                        QDateTimeEdit: down - button:focus
{
    background - color: qlineargradient(spread: pad, x1: 1, y1: 0.8, x2: 1, y2: 0, stop: 0  # 5e90fa, stop:1 #6f9efa);
}

QAbstractSpinBox: up - button:disabled,
                              QSpinBox: up - button:disabled,
                                                    QDoubleSpinBox: up - button:disabled,
                                                                                QTimeEdit: up - button:disabled,
                                                                                                       QDateEdit: up - button:disabled,
                                                                                                                              QDateTimeEdit: up - button:disabled,
                                                                                                                                                         QAbstractSpinBox: down - button:disabled,
                                                                                                                                                                                         QSpinBox: down - button:disabled,
                                                                                                                                                                                                                 QDoubleSpinBox: down - button:disabled,
                                                                                                                                                                                                                                               QTimeEdit: down - button:disabled,
                                                                                                                                                                                                                                                                        QDateEdit: down - button:disabled,
                                                                                                                                                                                                                                                                                                 QDateTimeEdit: down - button:disabled
{
    background - color: transparent;
}

QAbstractSpinBox::up - arrow,
                  QSpinBox::up - arrow,
                            QDoubleSpinBox::up - arrow,
                                            QTimeEdit::up - arrow,
                                                       QDateEdit::up - arrow,
                                                                  QDateTimeEdit::up - arrow
{
    image: url(qss: images / up_arrow_dark.png);
top: 2
px; / *fix
symmetry
between
up and down
images * /
}

QAbstractSpinBox::up - arrow: focus,
QSpinBox::up - arrow: focus,
QDoubleSpinBox::up - arrow: focus,
QTimeEdit::up - arrow: focus,
QDateEdit::up - arrow: focus,
QDateTimeEdit::up - arrow: focus
{
    image: url(qss: images / up_arrow_lighter.png);
}

QAbstractSpinBox::up - arrow: off,
QSpinBox::up - arrow: off,
QDoubleSpinBox::up - arrow: off,
QTimeEdit::up - arrow: off,
QDateEdit::up - arrow: off,
QDateTimeEdit::up - arrow: off
{
    image: url(qss: images / up_arrow_disabled_dark.png);
}

QAbstractSpinBox::up - arrow: disabled,
QSpinBox::up - arrow: disabled,
QDoubleSpinBox::up - arrow: disabled,
QTimeEdit::up - arrow: disabled,
QDateEdit::up - arrow: disabled,
QDateTimeEdit::up - arrow: disabled
{
    image: url(qss: images / up_arrow_disabled_dark.png);
}

QAbstractSpinBox::down - arrow,
                  QSpinBox::down - arrow,
                            QDoubleSpinBox::down - arrow,
                                            QTimeEdit::down - arrow,
                                                       QDateEdit::down - arrow,
                                                                  QDateTimeEdit::down - arrow
{
    image: url(qss: images / down_arrow_dark.png);
bottom: 0
px; / *fix
simetry
between
up and down
images * /
}

QAbstractSpinBox::down - arrow: focus,
QSpinBox::down - arrow: focus,
QDoubleSpinBox::down - arrow: focus,
QTimeEdit::down - arrow: focus,
QDateEdit::down - arrow: focus,
QDateTimeEdit::down - arrow: focus
{
    image: url(qss: images / down_arrow_lighter.png);
}

QAbstractSpinBox::down - arrow: off,
QSpinBox::down - arrow: off,
QDoubleSpinBox::down - arrow: off,
QTimeEdit::down - arrow: off,
QDateEdit::down - arrow: off,
QDateTimeEdit::down - arrow: off
{
    image: url(qss: images / down_arrow_disabled_dark.png);
}

QAbstractSpinBox::down - arrow: disabled,
QSpinBox::down - arrow: disabled,
QDoubleSpinBox::down - arrow: disabled,
QTimeEdit::down - arrow: disabled,
QDateEdit::down - arrow: disabled,
QDateTimeEdit::down - arrow: disabled
{
    image: url(qss: images / down_arrow_disabled_dark.png);
}

/ *ComboBox * /
   QComboBox::drop - down
{
    background - color:  # d2d2d2;
        subcontrol - origin: border; / *important * /
                                        subcontrol - position: top
right;
width: 20
px;
border - top - right - radius: 3
px;
border - bottom - right - radius: 3
px;
}

QComboBox::drop - down: on,
QComboBox::drop - down: focus
{
    background - color: qlineargradient(spread: pad, x1: 1, y1: 0.8, x2: 1, y2: 0, stop: 0  # 5e90fa, stop:1 #7cabf9);
}

QComboBox::down - arrow
{
    image: url(qss: images / down_arrow_dark.png);
}

QComboBox::down - arrow: on,
QComboBox::down - arrow: focus
{
    image: url(qss: images / down_arrow_lighter.png);
}

QComboBox::down - arrow: off,
QComboBox::down - arrow: disabled
{
    image: url(qss: images / down_arrow_disabled_dark.png);
}

/ *ComboBox
menu * /
QComboBox
{
    selection - color: white;
selection - background - color:  # 5e90fa;
}

QComboBox
QAbstractItemView
{
    color:  # 6e6e6e; /* same as regular QComboBox color */
        background - color: transparent;
selection - color: white;
selection - background - color:  # 5e90fa;
border - width: 5
px
0
px
5
px
0
px;
border - style: solid;
border - color: transparent;
margin: 0
px - 1
px
0
px
0
px; / *temporal: hack
for Mac...
    try it on Windows and Linux * /
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Push
button
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QPushButton
{
color:  # 6e6e6e;
text - align: center;
background - color: qlineargradient(spread:pad, x1: 0, y1: 0.3, x2: 0, y2: 1, stop: 0  # f5f5f5, stop:1 #e6e6e6);
border: 1
px
solid  # d2d2d2;
border - bottom - color:  # c3c3c3; /* simulates shadow under the button */
padding: 4
px
22
px;
margin: 4
px
4
px;
min - height: 16
px; / *same as QTabBar
QPushButton
min - width * /
border - radius: 4
px;
}

QPushButton: hover,
QPushButton: focus
{
    color: white;
border - color:  # 3874f2;
background - color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # 5e90fa, stop:1 #3874f2);
}

QPushButton: disabled,
QPushButton: disabled:checked
{
    color:  #000000;
        border - color:  # e6e6e6;
background - color:  # e6e6e6;
}

QPushButton: pressed
{
    background - color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # 3874f2, stop:1 #5e90fa);
}

QPushButton: checked
{
    background - color:  # 5e90fa;
        border - color:  # 3874f2;
}

/ *Color
Buttons * /
Gui - -ColorButton,
Gui - -ColorButton: disabled
{
    padding: 0px; / *reset * /
                     margin: 0
px; / *reset * /
}

Gui - -ColorButton
{
    background - color: qlineargradient(spread: pad, x1: 0, y1: 0.3, x2: 0, y2: 1, stop: 0  # f5f5f5, stop:1 #e6e6e6);
border: 1
px
solid  # d2d2d2;
border - bottom - color:  # c3c3c3; /* simulates shadow under the button */
}

Gui - -ColorButton: disabled
{
    border - color: transparent;
background - color: rgba(0, 0, 0, 10);
}

Gui - -ColorButton: hover,
Gui - -ColorButton: focus
{
    border - color:  # 3874f2;
        background - color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # 5e90fa, stop:1 #3874f2);
}

Gui - -ColorButton: pressed
{
    background - color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # 3874f2, stop:1 #5e90fa);
}

/ *Pushbutton
style
for "..." inside Placement cell which launches Placement tool * /
Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QPushButton {
background-color:  # b6b6b6;
    border: 1
px
solid  # 828282;
min - width: 16
px; / *reset
it
due
to
larger
value
on
regular
QPushButton, same or bigger
value as regular
QPushButton
min - height * /
border - radius: 0
px;
margin: 0
px; / *reset * /
       padding: 0
px; / *reset * /
}

/ *Fix
for Expressions description QFrame that is "broken" with initial reset * /
Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QWidget > QWidget > QFrame {
background-color:  # f5f5f5; /* main background color */
    border: 1
px
solid  # dcdcdc;
border - radius: 2
px;
padding: 2
px
6
px;
}

QPushButton: checked
{
    background - color:  # 5e90fa;
        border - color:  # 3874f2;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tool
button
inside
QDialogs
that
works as QPushButtons
         == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
/ *found
under
Tools -> Customize -> Macros -> Pixmap
"..."
button * /
QDialog
QToolButton
{
    color:  # 6e6e6e;
        text - align: center;
background - color: qlineargradient(spread:pad, x1: 0, y1: 0.3, x2: 0, y2: 1, stop: 0  # f5f5f5, stop:1 #e6e6e6);
border: 1
px
solid  # d2d2d2;
border - bottom - color:  # c3c3c3; /* simulates shadow under the button */
padding: 0
px; / *different
than
regular
QPushButton * /
margin: 2
px; / *different
than
regular
QPushButton * /
min - height: 16
px; / *same as QTabBar
QPushButton
min - width * /
border - radius: 4
px;
}

QDialog
QToolButton: hover,
QDialog
QToolButton: focus
{
    color: white;
border - color:  # 3874f2;
background - color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # 5e90fa, stop:1 #3874f2);
}

QDialog
QToolButton: disabled,
QDialog
QToolButton: disabled:checked
{
    color:  # b6b6b6;
        border - color:  # e6e6e6;
background - color:  # e6e6e6;
}

QDialog
QToolButton: pressed
{
    background - color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # 3874f2, stop:1 #5e90fa);
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tool
button
inside
Task
Panel
content
that
works as QPushButtons
         == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
/ *found
inside
Part
Design
Workbench and "make a draft on a face"
Task
panel
options * /
QSint - -ActionGroup
QFrame[


class ="content"] QToolButton {


color:  # 6e6e6e;
text - align: center;
background - color: qlineargradient(spread:pad, x1: 0, y1: 0.3, x2: 0, y2: 1, stop: 0  # f5f5f5, stop:1 #e6e6e6);
border: 1
px
solid  # d2d2d2;
border - bottom - color:  # c3c3c3; /* simulates shadow under the button */
padding: 2
px
6
px; / *different
than
regular
QPushButton * /
margin: 2
px; / *different
than
regular
QPushButton * /
min - height: 16
px; / *same as QTabBar
QPushButton
min - width * /
border - radius: 4
px;
}

QSint - -ActionGroup
QFrame[


class ="content"] QToolButton:hover,
                              QSint - -ActionGroup


QFrame[


class ="content"] QToolButton:focus


{
color: white;
border - color:  # 3874f2;
background - color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # 5e90fa, stop:1 #3874f2);
}

QSint - -ActionGroup
QFrame[


class ="content"] QToolButton:disabled,
                              QSint - -ActionGroup


QFrame[


class ="content"] QToolButton:disabled: checked


{
color:  # b6b6b6;
border - color:  # e6e6e6;
background - color:  # e6e6e6;
}

QSint - -ActionGroup
QFrame[


class ="content"] QToolButton:pressed


{
background - color: qlineargradient(spread:pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # 3874f2, stop:1 #5e90fa);
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Radio
button
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QRadioButton::indicator: unchecked
{
    color:  # 505050;
        background - color: rgba(0, 0, 0, 20);
border: 1
px
solid  # 505050;
}

QRadioButton::indicator: checked
{
    background - color:  # 5e90fa; /* QCheckBox has the same color */
        border: 1
px
solid  # 3874f2; /* QCheckBox has the same color */
image: url(qss:images / radiobutton_light.png);
}

QRadioButton,
QRadioButton: disabled
{
    color:  # 505050;
        padding: 3
px;
outline: none;
background - color: transparent;
}

QRadioButton::indicator
{
    width: 11px;
height: 11
px;
border - radius: 6
px;
}

QRadioButton::indicator: pressed
{
    border - color:  # adc5ed;
}

QRadioButton::indicator: disabled
{
    color:  # 6e6e6e;
        background - color: transparent;
border: 1
px
solid  # 6e6e6e;
}

QRadioButton: focus
{
    border: none;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Checkbox
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QCheckBox,
QCheckBox: disabled
{
    color:  # 505050;
        padding: 3
px;
outline: none;
background - color: transparent;
}

QCheckBox::indicator
{
    color:  # c8c8c8;
        background - color: rgba(0, 0, 0, 20);
border: 1
px
solid  # 505050;
width: 11
px;
height: 11
px;
border - radius: 2
px;
}

QCheckBox::indicator: pressed,
QCheckBox::indicator: non - exclusive:checked: pressed,
QCheckBox::indicator: indeterminate:pressed,
QCheckBox::indicator: checked:pressed
{
    border - color:  # adc5ed;
}

QCheckBox::indicator: checked
{
    background - color:  # 5e90fa; /* QRadioButton has the same color */
        border: 1
px
solid  # 3874f2; /* QRadioButton has the same color */
image: url(qss:images / checkbox_light.png);
}

QCheckBox: disabled
{
    color: rgba(0, 0, 0, 40);
background - color: transparent;
}

QCheckBox::indicator: disabled
{
    background - color: rgba(0, 0, 0, 20);
border: 1
px
solid
rgba(0, 0, 0, 20);
}

QCheckBox::indicator: indeterminate
{
    background - color:  # 5e90fa;
        border: 1
px
solid  # 3874f2;
image: url(qss:images / checkbox_indeterminate_light.png);
}

QCheckBox: focus
{
    border: none;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Checkboxs
inside
QListWidget and QTreeView
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QListWidget::indicator,
QTreeView::indicator
{
    color:  # c8c8c8;
        background - color: rgba(0, 0, 0, 20);
border: 1
px
solid  # 505050;
width: 11
px;
height: 11
px;
border - radius: 2
px;
}

/ *fix
for QTreeView: :
    indicator
loosing
its
margin * /
QTreeView::indicator
{
    margin: 3px;
}

QListWidget::indicator: selected,
QTreeView::indicator: selected
{
    background - color:  # e6e6e6;
}

QListWidget::indicator: checked:selected,
QListWidget::indicator: indeterminate:selected,
QTreeView::indicator: checked:selected,
QTreeView::indicator: indeterminate:selected
{
    background - color:  # 7cabf9; /* slighly lighter than default */
        border - color:  # 2053c0; /* slighly darker than default */
}

QListWidget::indicator: pressed,
QListWidget::indicator: non - exclusive:checked: pressed,
QListWidget::indicator: indeterminate:pressed,
QListWidget::indicator: checked:pressed,
QTreeView::indicator: pressed,
QTreeView::indicator: non - exclusive:checked: pressed,
QTreeView::indicator: indeterminate:pressed,
QTreeView::indicator: checked:pressed
{
    border - color:  # adc5ed;
}

QListWidget::indicator: checked,
QTreeView::indicator: checked
{
    background - color:  # 5e90fa; /* QRadioButton has the same color */
        border: 1
px
solid  # 3874f2; /* QRadioButton has the same color */
image: url(qss:images / checkbox_light.png);
}

QListWidget::indicator: disabled,
QTreeView::indicator: disabled
{
    background - color: rgba(0, 0, 0, 20);
border: 1
px
solid
rgba(0, 0, 0, 20);
}

QListWidget::indicator: indeterminate,
QTreeView::indicator: indeterminate
{
    background - color:  # 5e90fa;
        border: 1
px
solid  # 3874f2;
image: url(qss:images / checkbox_indeterminate_light.png);
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Slider
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QSlider,
QSlider: active,
QSlider:!active
{
    border: none;
background - color: transparent;
}

QSlider: horizontal
{
    padding: 0px 10px;
}

QSlider: vertical
{
    padding: 10px 0px;
}

QSlider::groove
{
    background - color: rgba(0, 0, 0, 30);
border: 1
px
solid
rgba(0, 0, 0, 40);
border - radius: 5
px;
margin: 4
px
0
px;
}

QSlider::groove: horizontal
{
    height: 8px;
}

QSlider::groove: vertical
{
    width: 8px;
}

QSlider::groove: horizontal:disabled,
QSlider::groove: vertical:disabled
{
    border - color:  # dcdcdc;
        background - color:  # dcdcdc;
}

QSlider::handle: horizontal,
QSlider::handle: vertical
{
    background - color:  # b6b6b6;
        border: 1
px
solid  # b6b6b6;
width: 14
px;
height: 14
px;
border - radius: 8
px;
}

QSlider::handle: horizontal
{
    margin: -4px 0;
}

QSlider::handle: vertical
{
    margin: 0 - 4px;
}

QSlider::handle: horizontal:hover,
QSlider::handle: vertical:hover,
QSlider::handle: horizontal:pressed,
QSlider::handle: vertical:pressed
{
    border - color:  # 5e90fa;
        background - color:  # 5e90fa;
}

QSlider::handle: horizontal:disabled,
QSlider::handle: vertical:disabled
{
    border - color:  # dcdcdc;
        background - color:  # dcdcdc;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Toolbar
buttons
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
/ *QToolBar > QComboBox, disabled
because
creates
different
margins
for body and drop - down button * /
    QToolBar > QAbstractSpinBox,
QToolBar > QSpinBox,
QToolBar > QDoubleSpinBox,
QToolBar > QLineEdit,
QToolBar > QTextEdit,
QToolBar > QTimeEdit,
QToolBar > QDateEdit,
QToolBar > QDateTimeEdit
{
    margin: 0px 2px;
padding: 0
px;
min - width: 70
px; / *necessary
to
show
its
content * /
}

QToolBar > QComboBox,
QToolBar > QAbstractSpinBox,
QToolBar > QSpinBox,
QToolBar > QDoubleSpinBox,
QToolBar > QLineEdit,
QToolBar > QTextEdit,
QToolBar > QTimeEdit,
QToolBar > QDateEdit,
QToolBar > QDateTimeEdit
{
    min - height: 0px; / *reset
it
inside
Tool
Bar
due
to
the
user
ability
to
set
the
"size of toolbar icons"
inside
Preferences * /
}

QToolBar > QPushButton
{
    padding: 0px;
margin: 1
px; / *doesn
't work with :left, :right:, :top or :bottom sub-controls */
min - width: 16
px; / *could
not be
larger
due
to
switchable
Preferences
"Size of toolbar icons" * /
min - height: 16
px; / *could
not be
larger
due
to
switchable
Preferences
"Size of toolbar icons" * /
border - radius: 4
px; / *same as regular
QPushButton * /
}

QToolBar > QPushButton: checked
{
    border: 1px solid  # 7cabf9;
    background - color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # cbd8e6, stop:1 #7cabf9);
}

QToolBar > QPushButton:!checked
{
    background - color: qlineargradient(spread: pad, x1: 0, y1: 0.3, x2: 0, y2: 1, stop: 0  # f5f5f5, stop:1 #e6e6e6);
border: 1
px
solid  # d2d2d2;
border - bottom - color:  # c3c3c3; /* simulates shadow under the button */
}

QToolBar > QPushButton: checked:hover
{
    border - color:  # 6f9efa;
}

QToolBar > QPushButton:!checked: hover
{
    color: black;
border - color:  # b6b6b6;
}

QToolBar > QPushButton: checked:pressed
{
    background - color:  # 7cabf9;
}

QToolBar > QPushButton:!checked: pressed
{
    background - color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # b6b6b6, stop:1 #e6e6e6);
}

QToolBar > QPushButton: checked:disabled,
                                QToolBar > QPushButton:!checked: disabled
{
    border: none;
background - color: transparent;
}

QToolBar > QToolButton
{
    margin: 2px;
padding: 2
px;
border - radius: 3
px;
}

QToolBar > QToolButton: hover
{
    background - color: rgba(0, 0, 0, 20);
}

QToolBar > QToolButton: pressed
{
    background - color: rgba(0, 0, 0, 30);
}

/ *ToolBar
menu
buttons(buttons
with drop - down menu) * /
QToolBar > QToolButton  # qt_toolbutton_menubutton {
padding-right: 20
px; / *Hack
to
add
more
width
to
buttons
with menu * /
     border: 1
px
solid
transparent;
border - radius: 3
px;
}

QToolBar > QToolButton
# qt_toolbutton_menubutton:hover,
QToolBar > QToolButton
# qt_toolbutton_menubutton:pressed,
QToolBar > QToolButton
# qt_toolbutton_menubutton:open {
border: 1
px
solid  # 7cabf9;
}

QToolBar
QToolButton::menu - button,
             QToolBar > QToolButton
# qt_toolbutton_menubutton::menu-button {
border: none;
border - top - right - radius: 3
px;
border - bottom - right - radius: 3
px;
width: 16
px; / *16
px
width + 4
px
for border = 20px allocated above * /
outline: none;
background - color: transparent;
}

QToolBar > QToolButton  # qt_toolbutton_menubutton::menu-button:hover,
QToolBar > QToolButton  # qt_toolbutton_menubutton::menu-button:pressed,
QToolBar > QToolButton  # qt_toolbutton_menubutton::menu-button:open {
background - color: qlineargradient(spread:pad, x1: 1, y1: 0.8, x2: 1, y2: 0, stop: 0  # 5e90fa, stop:1 #7cabf9);
}

QToolBar > QToolButton::menu - arrow
{
    background - image: url(qss: images / down_arrow_dark.png);
background - position: center
center;
background - repeat: none;
subcontrol - origin: padding;
subcontrol - position: bottom
right;
height: 10
px; / *same as arrow
image * /
}

QToolBar > QToolButton::menu - arrow: hover
{
    background - image: url(qss: images / down_arrow_lighter.png);
}

QToolBar > QToolButton::menu - arrow: open
{
    background - image: url(qss: images / down_arrow_lighter.png);
}

/ *when
QToolButton is checked: * /
QToolButton: checked
{
    border: 1px solid  # 7cabf9;
    background - color: rgba(124, 171, 249, 60); / *transparency
for  # 7cabf9 color */
}

QToolButton: checked:hover
{
    border: 1px solid  # 7cabf9;
    background - color: rgba(124, 171, 249, 80); / *transparency
for  # 7cabf9 color */
}

/ *The
"show more"
button(it
can
also
be
stylable
with "QToolBarExtension" * /
     QToolBar QToolButton  # qt_toolbar_ext_button {
margin: 0
px;
padding: 0
px;
/ *background - image: url(qss:images / more_dark.png); * /
image: transparent;
background - repeat: none;
background - position: center
left;
}

QToolBar
QToolButton  # qt_toolbar_ext_button:hover {
/ *background - image: url(qss:images / more_light.png); * /
border - color:  # e0e0e0;
background - color:  # e0e0e0;
}

QToolBar
QToolButton  # qt_toolbar_ext_button:on {
/ * background - image: url(qss:images / more_light.png); * /
border - color:  # e0e0e0;
background - color:  # e0e0e0;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tables(spreadsheets)
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /
QTableView
{
    gridline - color:  # d2d2d2;
        selection - color:  # 1b3774;
selection - background - color:  # cbd8e6;
}

QTableView::item: hover
{
    background - color: rgba(0, 0, 0, 10); / *temporal: is it
displayed in Linux or Windows? on
OSX
it
isn
't */
}

QTableView::item: disabled
{
    color:  # e6e6e6;
}

QTableView::item: selected
{
    color:  # 1b3774;
        border - color:  # cbd8e6; /* same as focused background color */
border - bottom - color:  # 7cabf9; /* same as focused border color */
}

/ *fix
for elements inside the cells * /
QTableView > QWidget > QComboBox,
QTableView > QWidget > QAbstractSpinBox,
QTableView > QWidget > QSpinBox,
QTableView > QWidget > QDoubleSpinBox,
QTableView > QWidget > QLineEdit,
QTableView > QWidget > QTextEdit,
QTableView > QWidget > QTimeEdit,
QTableView > QWidget > QDateEdit,
QTableView > QWidget > QDateTimeEdit,
QTableView > QWidget > QComboBox:drop - down,
                                 QTableView > QWidget > QAbstractSpinBox: up - button,
QTableView > QWidget > QSpinBox: up - button,
QTableView > QWidget > QDoubleSpinBox: up - button,
QTableView > QWidget > QTimeEdit: up - button,
QTableView > QWidget > QDateEdit: up - button,
QTableView > QWidget > QDateTimeEdit: up - button,
QTableView > QWidget > QAbstractSpinBox: down - button,
QTableView > QWidget > QSpinBox: down - button,
QTableView > QWidget > QDoubleSpinBox: down - button,
QTableView > QWidget > QTimeEdit: down - button,
QTableView > QWidget > QDateEdit: down - button,
QTableView > QWidget > QDateTimeEdit: down - button,
QTableView > QWidget > Gui - -ColorButton
{
    border - radius: 0px;
}

QTableView > QWidget > QComboBox,
QTableView > QWidget > QAbstractSpinBox,
QTableView > QWidget > QSpinBox,
QTableView > QWidget > QDoubleSpinBox,
QTableView > QWidget > QLineEdit,
QTableView > QWidget > QTextEdit,
QTableView > QWidget > QTimeEdit,
QTableView > QWidget > QDateEdit,
QTableView > QWidget > QDateTimeEdit
{
    color: black;
background - color: transparent;
border - color: transparent;
}

QTableView > QWidget > QComboBox: drop - down,
QTableView > QWidget > QAbstractSpinBox: up - button,
QTableView > QWidget > QSpinBox: up - button,
QTableView > QWidget > QDoubleSpinBox: up - button,
QTableView > QWidget > QTimeEdit: up - button,
QTableView > QWidget > QDateEdit: up - button,
QTableView > QWidget > QDateTimeEdit: up - button,
QTableView > QWidget > QAbstractSpinBox: down - button,
QTableView > QWidget > QSpinBox: down - button,
QTableView > QWidget > QDoubleSpinBox: down - button,
QTableView > QWidget > QTimeEdit: down - button,
QTableView > QWidget > QDateEdit: down - button,
QTableView > QWidget > QDateTimeEdit: down - button,
QTableView > QWidget > Gui - -ColorButton
{
    background - color: rgba(0, 0, 0, 30);
}

QTableView > QWidget > QComboBox: focus,
QTableView > QWidget > QAbstractSpinBox: focus,
QTableView > QWidget > QSpinBox: focus,
QTableView > QWidget > QDoubleSpinBox: focus,
QTableView > QWidget > QLineEdit: focus,
QTableView > QWidget > QTextEdit: focus,
QTableView > QWidget > QTimeEdit: focus,
QTableView > QWidget > QDateEdit: focus,
QTableView > QWidget > QDateTimeEdit: focus
{
    color:  # 1b3774;
        selection - color: white;
selection - background - color:  # 5e90fa;
border - color:  # cbd8e6;
background - color:  # cbd8e6;
}

QTableView > QWidget > QComboBox: disabled,
QTableView > QWidget > QAbstractSpinBox: disabled,
QTableView > QWidget > QSpinBox: disabled,
QTableView > QWidget > QDoubleSpinBox: disabled,
QTableView > QWidget > QLineEdit: disabled,
QTableView > QWidget > QTextEdit: disabled,
QTableView > QWidget > QTimeEdit: disabled,
QTableView > QWidget > QDateEdit: disabled,
QTableView > QWidget > QDateTimeEdit: disabled
{
    color: rgba(0, 0, 0, 120);
background - color: transparent;
border - color: transparent;
}

QTableView > QWidget > QComboBox: read - only,
QTableView > QWidget > QAbstractSpinBox: read - only,
QTableView > QWidget > QSpinBox: read - only,
QTableView > QWidget > QDoubleSpinBox: read - only,
QTableView > QWidget > QLineEdit: read - only,
QTableView > QWidget > QTextEdit: read - only,
QTableView > QWidget > QTimeEdit: read - only,
QTableView > QWidget > QDateEdit: read - only,
QTableView > QWidget > QDateTimeEdit: read - only
{
    color: black;
background - color: transparent;
border - color: transparent;
}

/ *= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
EXPERIMENTAL
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == * /

/ *Fix
for preventing elements in different rows to accidentaly overlap * /
QDialog QGroupBox QFrame {
margin: 2
px
0
px;
}

*[mandatoryField = "true"] {background - color: cyan }'''