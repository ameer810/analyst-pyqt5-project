# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search by date widget2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(672, 338)
        Form.setStyleSheet("\n"
"/*\n"
"ABOUT\n"
"============================================================================================================\n"
"version 2.05\n"
"QT theme (stylesheet) specially developed for FreeCAD (http://www.freecadweb.org/).\n"
"It might work with other software that uses QT styling.\n"
"\n"
"\n"
"LICENSE\n"
"============================================================================================================\n"
"Copyright (c) 2016 Pablo Gil Fern?ndez\n"
"\n"
"This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.\n"
"To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.\n"
"\n"
"\n"
"INSTALLATION\n"
"============================================================================================================\n"
"1) Place the .qss files and /images/ folder in the path that fits your OS:\n"
"    OSX = /Users/[YOUR_USER_NAME]/Library/Preferences/FreeCAD/Gui/Stylesheets/\n"
"    WINDOWS = C:/[INSTALLATION_PATH]/FreeCAD/data/Gui/Stylesheets/\n"
"    LINUX = /home/[YOUR_USER_NAME]/.FreeCAD/Gui/Stylesheets/\n"
"\n"
"2) In order to display correctly images:\n"
"    2.1) FreeCAD 0.16 (development builds newer than commit 5b3d50a): that\'s it, you are done!\n"
"\n"
"    2.2) FreeCAD 0.15: Images used in the theme need ABSOLUTE paths to be found by FreeCAD, so you should search the string \"qss:images\" (without \"\") and replace with the real path of your computer. It should be done with all the .qss files you want to install-use\n"
"        find = qss:images\n"
"        replace = /Users/myName/Library/Preferences/FreeCAD/Gui/Stylesheets/images\n"
"\n"
"\n"
"CUSTOMIZATION\n"
"============================================================================================================\n"
"If you would like to change the overall look/style of the theme, just find and replace following colors in the whole file:\n"
"    BACKGROUND (darker to ligher)\n"
"        black\n"
"        #505050\n"
"        #6e6e6e\n"
"        #828282\n"
"        #a2a2a0\n"
"        #b6b6b6\n"
"        #c8c8c8\n"
"        #c3c3c3\n"
"        #d2d2d2\n"
"        #dcdcdc\n"
"        #e0e0e0\n"
"        #e6e6e6\n"
"        #f0f0f0\n"
"        #f5f5f5 = main background color\n"
"        white\n"
"\n"
"    SELECTION (darker to lighter)\n"
"        #1b3774\n"
"        #2053c0\n"
"        #3874f2\n"
"        #5e90fa = main selection color\n"
"        #6f9efa = used to build QSpinBox up and down buttons, it\'s used as color in the middle\n"
"        #7cabf9\n"
"        #adc5ed\n"
"        #cbd8e6\n"
"\n"
"\n"
"\n"
"\n"
"KNOWN BUGS and TO DO\n"
"============================================================================================================\n"
"    - please, follow the link to get updated information: http://forum.freecadweb.org/viewtopic.php?f=10&t=12417\n"
"*/\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Reset elements\n"
"==================================================================================================*/\n"
"/* Reseting everything helps to unify styles across different operating systems */\n"
"* {\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
"    border-style: none;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"/* specific reset for elements inside QToolBar */\n"
"QToolBar * {\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Main window\n"
"==================================================================================================*/\n"
"QMainWindow,\n"
"QDialog,\n"
"QDockWidget,\n"
"QToolBar  {\n"
"    background-color: #f5f5f5; /* main background color */\n"
"}\n"
"\n"
"QMdiArea {\n"
"    background-image: url(qss:images/background_freecad.png);\n"
"    background-position: center center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"MENUS\n"
"==================================================================================================*/\n"
"QMenuBar,\n"
"QMenuBar::item {\n"
"    color: black;\n"
"    background-color: #f5f5f5; /* main background color */\n"
"}\n"
"\n"
"QMenu,\n"
"QMenu::item {\n"
"    color: black;\n"
"    background-color: #f5f5f5; /* main background color */\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QMenuBar::item:selected,\n"
"QMenuBar::item:pressed,\n"
"QMenu::item:selected,\n"
"QMenu::item:pressed {\n"
"    color: white;\n"
"    background-color: #5e90fa;\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    image:url(qss:images/right_arrow_dark.png);\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QMenu::right-arrow:selected {\n"
"    image:url(qss:images/right_arrow_lighter.png);\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 2px 16px 2px 26px; /* make room for icon at left */\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::icon {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: rgba(0,0,0,30);\n"
"    margin: 6px 4px;\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    color: white;\n"
"}\n"
"\n"
"/* Fix for elements inside a drop-down menu */\n"
"QMenu QRadioButton,\n"
"QMenu QCheckBox,\n"
"QMenu QPushButton,\n"
"QMenu QToolButton {\n"
"    color: black; /* same as regular QRadioButton and QCheckBox */\n"
"}\n"
"\n"
"QMenu QRadioButton:hover,\n"
"QMenu QCheckBox:hover,\n"
"QMenu QPushButton:hover,\n"
"QMenu QToolButton:hover,\n"
"QMenu QPushButton:pressed,\n"
"QMenu QToolButton:pressed,\n"
"QMenu QPushButton:selected,\n"
"QMenu QToolButton:selected {\n"
"    color: white;\n"
"    background-color: #5e90fa; /* same as QMenu::item:selected and QMenu::item:pressed */\n"
"}\n"
"\n"
"QMenu QRadioButton:disabled,\n"
"QMenu QCheckBox:disabled {\n"
"    color: #6e6e6e;\n"
"}\n"
"\n"
"QMenu QRadioButton::indicator:disabled,\n"
"QMenu QCheckBox::indicator:disabled {\n"
"    color: #6e6e6e;\n"
"    background-color: transparent;\n"
"    border: 1px solid #6e6e6e;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tool bar\n"
"==================================================================================================*/\n"
"QToolBar {\n"
"    border: none;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolBar::handle:top,\n"
"QToolBar::handle:bottom,\n"
"QToolBar::handle:horizontal {\n"
"    background-image: url(qss:images/Hmovetoolbar_dark.png);\n"
"    width: 10px;\n"
"    margin: 4px 2px;\n"
"    background-position: top right;\n"
"    background-repeat: repeat-y;\n"
"}\n"
"\n"
"QToolBar::handle:left,\n"
"QToolBar::handle:right,\n"
"QToolBar::handle:vertical {\n"
"    background-image: url(qss:images/Vmovetoolbar_dark.png);\n"
"    height: 10px;\n"
"    margin: 2px 4px;\n"
"    background-position: left bottom;\n"
"    background-repeat: repeat-x;\n"
"}\n"
"\n"
"QToolBar::separator:top,\n"
"QToolBar::separator:bottom,\n"
"QToolBar::separator:horizontal {\n"
"    width: 1px;\n"
"    margin: 6px 4px;\n"
"    background-color: rgba(0,0,0,30);\n"
"}\n"
"\n"
"QToolBar::separator:left,\n"
"QToolBar::separator:right,\n"
"QToolBar::separator:vertical {\n"
"    height: 1px;\n"
"    margin: 4px 6px;\n"
"    background-color: rgba(0,0,0,30);\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Group box\n"
"==================================================================================================*/\n"
"QGroupBox {\n"
"    color: rgba(0,0,0,120);\n"
"    border:1px solid rgba(0, 0, 0, 20); /* lighter than its own border-color */;\n"
"    border-radius: 3px;\n"
"    margin-top: 10px;\n"
"    padding: 6px;\n"
"    background-color: rgba(255, 255, 255, 15);\n"
"}\n"
"\n"
"QGroupBox:title {\n"
"    top: -8px;\n"
"    left: 12px;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tooltip\n"
"==================================================================================================*/\n"
"QToolTip {\n"
"    color: white;\n"
"    background-color: #828282;\n"
"    /*opacity: 90%; doesn\'t correctly work */\n"
"    padding: 4px;\n"
"    border-radius: 3px; /* has no effect */\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Dock widget\n"
"==================================================================================================*/\n"
"QDockWidget {\n"
"    color: rgba(0,0,0,120);\n"
"    titlebar-close-icon: url(qss:images/close_dark.png);\n"
"    titlebar-normal-icon: url(qss:images/undock_dark.png);\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    text-align: center;\n"
"    background-color: rgba(0,0,0,10);\n"
"    border: 4px solid #f5f5f5; /* fix to simulate margin between this :title and tabs */ /* same as main background color */\n"
"    border-radius: 6px; /* bigger than normal due to previous border fix */\n"
"    padding: 4px 0px; /* also needed because of previous border fix */\n"
"}\n"
"\n"
"QDockWidget::close-button,\n"
"QDockWidget::float-button {\n"
"    border: none;\n"
"    background: transparent;\n"
"    border-radius: 3px;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"    right: 4px;\n"
"}\n"
"    \n"
"QDockWidget::float-button {\n"
"    right: 22px;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover,\n"
"QDockWidget::float-button:hover {\n"
"    background-color: rgba(0,0,0,15);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed,\n"
"QDockWidget::float-button:pressed {\n"
"    background-color: rgba(0,0,0,30);\n"
"}\n"
"\n"
"/* fix for Python Console (probably there is a smarter way to arrive to it) */\n"
"QDockWidget > QFrame {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #c3c3c3;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Progress bar\n"
"==================================================================================================*/\n"
"QProgressBar,\n"
"QProgressBar:horizontal {\n"
"    color: white;\n"
"    background-color: rgba(0,0,0,10);\n"
"    text-align: center;\n"
"    border: 1px solid rgba(0,0,0,80);\n"
"    padding: 1px;\n"
"    border-radius: 3px;\n"
"}\n"
"QProgressBar::chunk,\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #3874f2, stop:1 #5e90fa);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Scroll\n"
"==================================================================================================*/\n"
"QAbstractScrollArea {\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover,\n"
"QScrollBar::handle:horizontal:hover {\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 5px;\n"
"    border-radius: 3px;\n"
"    margin: 4px 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    margin: 1px 3px 0px 3px; /* 1px to correctly fit the 10px width image */\n"
"    border-image: url(qss:images/left_arrow_dark.png);\n"
"    width: 6px;\n"
"    height: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    margin: 1px 3px 0px 3px; /* 1px to correctly fit the 10px width image */\n"
"    border-image: url(qss:images/right_arrow_dark.png);\n"
"    width: 6px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:on {\n"
"    border-image: url(qss:images/left_arrow_darker.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::add-line:horizontal:on {\n"
"    border-image: url(qss:images/right_arrow_darker.png);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 15px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 5px;\n"
"    border-radius: 3px;\n"
"    margin: 15px 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    margin: 3px 0px 3px 1px; /* 1px to correctly fit the 10px width image */\n"
"    border-image: url(qss:images/up_arrow_dark.png);\n"
"    height: 6px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    margin: 3px 0px 3px 1px; /* 1px to correctly fit the 10px width image */\n"
"    border-image: url(qss:images/down_arrow_dark.png);\n"
"    height: 6px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:on {\n"
"    border-image: url(qss:images/up_arrow_darker.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::add-line:vertical:on {\n"
"    border-image: url(qss:images/down_arrow_darker.png);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Tab bar\n"
"==================================================================================================*/\n"
"QTabWidget::pane {\n"
"    background-color: transparent; /* temporal (transparent background) */ /* tab content background color */\n"
"    position: absolute;\n"
"}\n"
"\n"
"QTabWidget::pane:top {\n"
"    top: -1px;\n"
"    border-top: 1px solid #d2d2d2;\n"
"}\n"
"\n"
"QTabWidget::pane:bottom {\n"
"    bottom: -1px;\n"
"    border-bottom: 1px solid #d2d2d2;\n"
"}\n"
"\n"
"QTabWidget::pane:left {\n"
"    right: -1px;\n"
"    border-right: 1px solid #d2d2d2;\n"
"}\n"
"\n"
"QTabWidget::pane:right {\n"
"    left: -1px;\n"
"    border-left: 1px solid #d2d2d2;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top,\n"
"QTabWidget::tab-bar:bottom {\n"
"    left: 10px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left,\n"
"QTabWidget::tab-bar:right {\n"
"    top: 10px;\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0; /* important */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Workaround for QTabBars created from docked QDockWidgets which don\'t draw the border if not set and reseted as follows: */\n"
"QTabBar {\n"
"    border-top: 1px solid #d2d2d2;  /* set color for all QTabBars */\n"
"}\n"
"QDockWidget QTabBar {\n"
"    border-color: transparent; /* set color for all QTabBars but ones created from QDockWidget */\n"
"}\n"
"QDialog QTabBar {\n"
"    border-color: transparent; /* set color for QTabBars inside Preferences dialog */\n"
"}\n"
"/* end fix */\n"
"\n"
"QTabBar::tab {\n"
"    background-color: transparent;\n"
"    border: 1px solid transparent;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top,\n"
"QTabBar::tab:bottom {\n"
"    border-top-width: 4px}\n"
"/*==================================================================================================\n"
"Buttons\n"
"==================================================================================================*/\n"
"/* Common */\n"
"QComboBox,\n"
"QAbstractSpinBox,\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QLineEdit,\n"
"QTextEdit,\n"
"QTimeEdit,\n"
"QDateEdit,\n"
"QDateTimeEdit {\n"
"    color: #6e6e6e;\n"
"    background-color: #e0e0e0;\n"
"    selection-color: white;\n"
"    selection-background-color: #5e90fa;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 3px;\n"
"    min-width: 50px; /* it ensures the default value is correctly displayed */\n"
"    min-height: 20px; /* important to be a pair number in order to up/down buttons to be divisible by two (if not set could create a blank line in Ubuntu. Its downside is that it\'s needed to reset it (min-width: 0px) on following elements that can\'t have it such as fields inside QToolBar and inside QTreeView (Property editor) */\n"
"    padding: 1px 2px; /* temporal: could don\'t be compatible with elements inside Tree/List view */\n"
"}\n"
"\n"
"/* shifts text/number editable field to the left to make space for the up/down or drop-down buttons */\n"
"QComboBox,\n"
"QAbstractSpinBox,\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QTimeEdit,\n"
"QDateEdit,\n"
"QDateTimeEdit {\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"/* when QTextEdit are no editable */\n"
"QTextEdit:!editable {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #c3c3c3;\n"
"}\n"
"\n"
"QComboBox:focus,\n"
"QAbstractSpinBox:focus,\n"
"QSpinBox:focus,\n"
"QDoubleSpinBox:focus,\n"
"QLineEdit:focus,\n"
"QTextEdit:focus,\n"
"QTimeEdit:focus,\n"
"QDateEdit:focus,\n"
"QDateTimeEdit:focus {\n"
"    color: black;\n"
"    border-color: #7cabf9;\n"
"    border-right-color: qlineargradient(spread:pad, x1:1, y1:0.8, x2:1, y2:0, stop:0 #5e90fa, stop:1 #7cabf9); /* same as up/down or drop-down button color */\n"
"    background-color: #cbd8e6;\n"
"}\n"
"\n"
"QComboBox:disabled,\n"
"QAbstractSpinBox:disabled,\n"
"QSpinBox:disabled,\n"
"QDoubleSpinBox:disabled,\n"
"QLineEdit:disabled,\n"
"QTextEdit:disabled,\n"
"QTimeEdit:disabled,\n"
"QDateEdit:disabled,\n"
"QDateTimeEdit:disabled {\n"
"    color: #c3c3c3;\n"
"    background-color: #e0e0e0; /* same as enabled color */\n"
"    border-color: #e0e0e0; /* same as enabled color */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button,\n"
"QSpinBox:up-button,\n"
"QDoubleSpinBox:up-button,\n"
"QTimeEdit:up-button,\n"
"QDateEdit:up-button,\n"
"QDateTimeEdit:up-button,\n"
"QAbstractSpinBox:down-button,\n"
"QSpinBox:down-button,\n"
"QDoubleSpinBox:down-button,\n"
"QTimeEdit:down-button,\n"
"QDateEdit:down-button,\n"
"QDateTimeEdit:down-button {\n"
"    background-color: #d2d2d2;\n"
"    subcontrol-origin: border; /* important */\n"
"    width: 20px; /* same as QComboBox ... QDateTimeEdit padding-right */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button,\n"
"QSpinBox:up-button,\n"
"QDoubleSpinBox:up-button,\n"
"QTimeEdit:up-button,\n"
"QDateEdit:up-button,\n"
"QDateTimeEdit:up-button {\n"
"    subcontrol-position: top right;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button,\n"
"QSpinBox:down-button,\n"
"QDoubleSpinBox:down-button,\n"
"QTimeEdit:down-button,\n"
"QDateEdit:down-button,\n"
"QDateTimeEdit:down-button {\n"
"    subcontrol-position: bottom right;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button:focus,\n"
"QSpinBox:up-button:focus,\n"
"QDoubleSpinBox:up-button:focus,\n"
"QTimeEdit:up-button:focus,\n"
"QDateEdit:up-button:focus,\n"
"QDateTimeEdit:up-button:focus {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.8, x2:1, y2:0, stop:0 #6f9efa, stop:1 #7cabf9);\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button:focus,\n"
"QSpinBox:down-button:focus,\n"
"QDoubleSpinBox:down-button:focus,\n"
"QTimeEdit:down-button:focus,\n"
"QDateEdit:down-button:focus,\n"
"QDateTimeEdit:down-button:focus {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.8, x2:1, y2:0, stop:0 #5e90fa, stop:1 #6f9efa);\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button:disabled,\n"
"QSpinBox:up-button:disabled,\n"
"QDoubleSpinBox:up-button:disabled,\n"
"QTimeEdit:up-button:disabled,\n"
"QDateEdit:up-button:disabled,\n"
"QDateTimeEdit:up-button:disabled,\n"
"QAbstractSpinBox:down-button:disabled,\n"
"QSpinBox:down-button:disabled,\n"
"QDoubleSpinBox:down-button:disabled,\n"
"QTimeEdit:down-button:disabled,\n"
"QDateEdit:down-button:disabled,\n"
"QDateTimeEdit:down-button:disabled {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow,\n"
"QTimeEdit::up-arrow,\n"
"QDateEdit::up-arrow,\n"
"QDateTimeEdit::up-arrow {\n"
"    image: url(qss:images/up_arrow_dark.png);\n"
"    top: 2px; /* fix symmetry between up and down images */\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:focus,\n"
"QSpinBox::up-arrow:focus,\n"
"QDoubleSpinBox::up-arrow:focus,\n"
"QTimeEdit::up-arrow:focus,\n"
"QDateEdit::up-arrow:focus,\n"
"QDateTimeEdit::up-arrow:focus {\n"
"    image: url(qss:images/up_arrow_lighter.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:off,\n"
"QSpinBox::up-arrow:off,\n"
"QDoubleSpinBox::up-arrow:off,\n"
"QTimeEdit::up-arrow:off,\n"
"QDateEdit::up-arrow:off,\n"
"QDateTimeEdit::up-arrow:off {\n"
"    image: url(qss:images/up_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:disabled,\n"
"QSpinBox::up-arrow:disabled,\n"
"QDoubleSpinBox::up-arrow:disabled,\n"
"QTimeEdit::up-arrow:disabled,\n"
"QDateEdit::up-arrow:disabled,\n"
"QDateTimeEdit::up-arrow:disabled {\n"
"    image: url(qss:images/up_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow,\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow,\n"
"QTimeEdit::down-arrow,\n"
"QDateEdit::down-arrow,\n"
"QDateTimeEdit::down-arrow {\n"
"    image: url(qss:images/down_arrow_dark.png);\n"
"    bottom: 0px; /* fix simetry between up and down images */\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:focus,\n"
"QSpinBox::down-arrow:focus,\n"
"QDoubleSpinBox::down-arrow:focus,\n"
"QTimeEdit::down-arrow:focus,\n"
"QDateEdit::down-arrow:focus,\n"
"QDateTimeEdit::down-arrow:focus {\n"
"    image: url(qss:images/down_arrow_lighter.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:off,\n"
"QSpinBox::down-arrow:off,\n"
"QDoubleSpinBox::down-arrow:off,\n"
"QTimeEdit::down-arrow:off,\n"
"QDateEdit::down-arrow:off,\n"
"QDateTimeEdit::down-arrow:off {\n"
"    image: url(qss:images/down_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:disabled,\n"
"QDoubleSpinBox::down-arrow:disabled,\n"
"QTimeEdit::down-arrow:disabled,\n"
"QDateEdit::down-arrow:disabled,\n"
"QDateTimeEdit::down-arrow:disabled {\n"
"    image: url(qss:images/down_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox::drop-down {\n"
"    background-color: #d2d2d2;\n"
"    subcontrol-origin: border; /* important */\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:on,\n"
"QComboBox::drop-down:focus {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.8, x2:1, y2:0, stop:0 #5e90fa, stop:1 #7cabf9);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(qss:images/down_arrow_dark.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QComboBox::down-arrow:focus {\n"
"    image: url(qss:images/down_arrow_lighter.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:off,\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(qss:images/down_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"/* ComboBox menu */\n"
"QComboBox {\n"
"    selection-color: white;\n"
"    selection-background-color: #5e90fa;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #6e6e6e; /* same as regular QComboBox color */\n"
"    background-color: transparent;\n"
"    selection-color: white;\n"
"    selection-background-color: #5e90fa;\n"
"    border-width: 5px 0px 5px 0px;\n"
"    border-style: solid;\n"
"    border-color: transparent;\n"
"    margin: 0px -1px 0px 0px; /* temporal: hack for Mac... try it on Windows and Linux */\n"
"}\n"
"\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Radio button\n"
"==================================================================================================*/\n"
"QRadioButton::indicator:unchecked{\n"
"    color: #505050;\n"
"    background-color: rgba(0, 0, 0, 20);\n"
"    border: 1px solid #505050;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #5e90fa; /* QCheckBox has the same color */\n"
"    border: 1px solid #3874f2; /* QCheckBox has the same color */\n"
"    image:url(qss:images/radiobutton_light.png);\n"
"}\n"
"\n"
"QRadioButton,\n"
"QRadioButton:disabled {\n"
"    color: #505050;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 11px;\n"
"    height: 11px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    border-color: #adc5ed;\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled {\n"
"    color: #6e6e6e;\n"
"    background-color: transparent;\n"
"    border: 1px solid #6e6e6e;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/*==================================================================================================\n"
"Checkbox\n"
"==================================================================================================*/\n"
"QCheckBox,\n"
"QCheckBox:disabled {\n"
"    color: #505050;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    color: #c8c8c8;\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid #505050;\n"
"    width: 11px;\n"
"    height: 11px;\n"
"    border-radius:2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:pressed,\n"
"QCheckBox::indicator:non-exclusive:checked:pressed,\n"
"QCheckBox::indicator:indeterminate:pressed,\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border-color: #adc5ed;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #5e90fa; /* QRadioButton has the same color */\n"
"    border: 1px solid #3874f2; /* QRadioButton has the same color */\n"
"    image:url(qss:images/checkbox_light.png);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgba(0,0,0,40);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: rgba(0,0,0,20);\n"
"    border: 1px solid rgba(0,0,0,20);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"    background-color: #5e90fa;\n"
"    border: 1px solid #3874f2;\n"
"    image: url(qss:images/checkbox_indeterminate_light.png);\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*==================================================================================================\n"
"EXPERIMENTAL\n"
"==================================================================================================*/\n"
"\n"
"/* Fix for preventing elements in different rows to accidentaly overlap */\n"
"QDialog QGroupBox QFrame {\n"
"    margin: 2px 0px;\n"
"}\n"
"\n"
"*[mandatoryField=\"true\"] { background-color: cyan }\n"
"QPushButton {\n"
"    border-radius: 20px;\n"
"    color: rgb(230, 230, 230);\n"
"    text-align: center;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2);\n"
"    border: 1px solid #d2d2d2;\n"
"    border-bottom-color: #c3c3c3; /* simulates shadow under the button */\n"
"    padding: 4px 22px;\n"
"    margin: 4px 4px;\n"
"    min-height: 16px; /* same as QTabBar QPushButton min-width */\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"    color: white;\n"
"    border: 1px solid rgb(49, 44, 113);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.512438 rgba(69, 124, 225, 255), stop:1 rgba(82, 157, 255, 255))\n"
"}\n"
"\n"
"QPushButton:disabled,\n"
"QPushButton:disabled:checked {\n"
"    color: #b6b6b6;\n"
"    border-color: #e6e6e6;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3874f2, stop:1 #5e90fa);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(35, 72, 147);\n"
"    border-color: #3874f2;\n"
"}\n"
"\n"
"/* Color Buttons */\n"
"Gui--ColorButton,\n"
"Gui--ColorButton:disabled {\n"
"    padding: 0px; /* reset */\n"
"    margin: 0px; /* reset */\n"
"}\n"
"\n"
"Gui--ColorButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.3, x2:0, y2:1, stop:0 #f5f5f5, stop:1 #e6e6e6);\n"
"    border: 1px solid #d2d2d2;\n"
"    border-bottom-color: #c3c3c3; /* simulates shadow under the button */\n"
"}\n"
"\n"
"Gui--ColorButton:disabled {\n"
"    border-color: transparent;\n"
"    background-color: rgba(0,0,0,10);\n"
"}\n"
"\n"
"Gui--ColorButton:hover,\n"
"Gui--ColorButton:focus {\n"
"    border-color: #3874f2;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5e90fa, stop:1 #3874f2);\n"
"}\n"
"\n"
"Gui--ColorButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #3874f2, stop:1 #5e90fa);\n"
"}\n"
"\n"
"/* Pushbutton style for \"...\" inside Placement cell which launches Placement tool */\n"
"Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QPushButton {\n"
"    background-color: #b6b6b6;\n"
"    border: 1px solid #828282;\n"
"    min-width: 16px; /* reset it due to larger value on regular QPushButton, same or bigger value as regular QPushButton min-height */\n"
"    border-radius: 0px;\n"
"    margin: 0px; /* reset */\n"
"    padding: 0px; /* reset */\n"
"}\n"
"\n"
"/* Fix for Expressions description QFrame that is \"broken\" with initial reset */\n"
"Gui--PropertyEditor--PropertyEditor > QWidget > QWidget > QWidget > QWidget > QFrame {\n"
"    background-color: #f5f5f5; /* main background color */\n"
"    border: 1px solid #dcdcdc;\n"
"    border-radius: 2px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #5e90fa;\n"
"    border-color: #3874f2;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(410, 30, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(90, 30, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.spinBox.setStyleSheet("border-radius:23px")
        self.spinBox.setMaximum(1000000017)
        self.spinBox.setObjectName("spinBox")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 651, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(270, -10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.label_67 = QtWidgets.QLabel(self.groupBox)
        self.label_67.setGeometry(QtCore.QRect(254, 64, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_5.setGeometry(QtCore.QRect(20, 60, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_5.setFont(font)
        self.dateEdit_5.setStyleSheet("border-radius:20px;")
        self.dateEdit_5.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_5.setCalendarPopup(True)
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.label_66 = QtWidgets.QLabel(self.groupBox)
        self.label_66.setGeometry(QtCore.QRect(580, 60, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.dateEdit_6 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_6.setGeometry(QtCore.QRect(380, 62, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_6.setFont(font)
        self.dateEdit_6.setStyleSheet("border-radius:20px;")
        self.dateEdit_6.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_6.setCalendarPopup(True)
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.label_68 = QtWidgets.QLabel(self.groupBox)
        self.label_68.setGeometry(QtCore.QRect(320, 60, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_20.setGeometry(QtCore.QRect(200, 150, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_20.setStyleSheet("border-radius:26px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons8-search-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_20.setIcon(icon)
        self.pushButton_20.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_20.setObjectName("pushButton_20")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "الرقم التعريفي للمراجع"))
        self.label_2.setText(_translate("Form", "التاريخ"))
        self.label_67.setText(_translate("Form", "الى"))
        self.label_66.setText(_translate("Form", "من"))
        self.label_68.setText(_translate("Form", "|"))
        self.pushButton_20.setText(_translate("Form", "بحث"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
