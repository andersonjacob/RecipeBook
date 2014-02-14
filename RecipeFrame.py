#
# generated by wxGlade 0.6.8 on Tue Dec 10 14:29:11 2013
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class RecipeFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: RecipeFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.txtTitle = wx.TextCtrl(self, wx.ID_ANY, _("Recipe Title"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Contributor"))
        self.txtAuthor = wx.TextCtrl(self, wx.ID_ANY, _("author name"))
        self.splitter = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.topPanel = wx.Panel(self.splitter, wx.ID_ANY, style=wx.NO_BORDER)
        self.IngredientList = wx.ListView(self.topPanel, wx.ID_ANY, style=wx.LC_REPORT)
        self.IngredientList.InsertColumn(0, 'quantity', format=wx.LIST_FORMAT_RIGHT, width=wx.LIST_AUTOSIZE)
        self.IngredientList.InsertColumn(1, 'ingredient',width=wx.LIST_AUTOSIZE)
        self.IngredientList.InsertStringItem(0, "1 bunch")
        self.IngredientList.SetStringItem(0, 1, "of lots of good stuff")
        icnt = self.IngredientList.GetItemCount()
        self.IngredientList.InsertStringItem(icnt, "1 additional squirt")
        self.IngredientList.SetStringItem(icnt, 1, "of really yummy topping")
        self.IngredientList.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.IngredientList.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.panel_1 = wx.Panel(self.topPanel, wx.ID_ANY, style=wx.NO_BORDER)
        self.btnAddIngredient = wx.Button(self.panel_1, wx.ID_ADD, _("Add Ingredient"))
        self.btnRmIngredient = wx.Button(self.panel_1, wx.ID_REMOVE, _("Remove Ingredient"))
        self.btnUpIngredient = wx.Button(self.panel_1, wx.ID_UP, _("Move Up"))
        self.btnDwIngredient = wx.Button(self.panel_1, wx.ID_DOWN, _("Move Down"))
        self.bottomPanel = wx.Panel(self.splitter, wx.ID_ANY, style=wx.NO_BORDER)
        self.label_1 = wx.StaticText(self.bottomPanel, wx.ID_ANY, _("Recipe Instructions"))
        self.txtRecipe = wx.TextCtrl(self.bottomPanel, wx.ID_ANY, _("This is the default text,\nWith two lines.\nThis is are really really really really really really really long line that I am hoping will automagically wrap in the text box."), style=wx.TE_MULTILINE)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Yield"))
        self.txtYield = wx.TextCtrl(self, wx.ID_ANY, _("1 bunch of good stuff"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("Prep Time"))
        self.txtPrep = wx.TextCtrl(self, wx.ID_ANY, _("0 minutes"))
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Cook Time"))
        self.txtCook = wx.TextCtrl(self, wx.ID_ANY, _("0 min"))
        self.btnPanel = wx.Panel(self, wx.ID_ANY)
        self.btnSave = wx.Button(self.btnPanel, wx.ID_SAVE, _("&Save"))
        self.btnCancel = wx.Button(self.btnPanel, wx.ID_CANCEL, _("&Cancel"))
        self.btnPrev = wx.Button(self.btnPanel, wx.ID_BACKWARD, _("<&Previous"))
        self.btnNext = wx.Button(self.btnPanel, wx.ID_FORWARD, _("&Next >"))
        self.btnOpen = wx.Button(self.btnPanel, wx.ID_OPEN, _("&Open Recipe"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: RecipeFrame.__set_properties
        self.SetTitle(_("Recipes"))
        self.SetSize((800, 600))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: RecipeFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.txtTitle, 0, wx.EXPAND, 0)
        sizer_1.Add(self.label_2, 0, 0, 0)
        sizer_1.Add(self.txtAuthor, 0, wx.EXPAND, 0)
        sizer_2.Add(self.IngredientList, 1, wx.EXPAND, 0)
        sizer_4.Add(self.btnAddIngredient, 0, wx.LEFT | wx.BOTTOM, 1)
        sizer_4.Add(self.btnRmIngredient, 0, wx.BOTTOM, 1)
        sizer_4.Add(self.btnUpIngredient, 0, wx.BOTTOM, 1)
        sizer_4.Add(self.btnDwIngredient, 0, wx.BOTTOM, 1)
        self.panel_1.SetSizer(sizer_4)
        sizer_2.Add(self.panel_1, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.topPanel.SetSizer(sizer_2)
        sizer_3.Add(self.label_1, 0, 0, 0)
        sizer_3.Add(self.txtRecipe, 1, wx.EXPAND, 0)
        self.bottomPanel.SetSizer(sizer_3)
        self.splitter.SplitHorizontally(self.topPanel, self.bottomPanel)
        sizer_1.Add(self.splitter, 1, wx.EXPAND, 0)
        sizer_1.Add(self.label_3, 0, 0, 0)
        sizer_1.Add(self.txtYield, 0, wx.EXPAND, 0)
        sizer_1.Add(self.label_4, 0, 0, 0)
        sizer_1.Add(self.txtPrep, 0, wx.EXPAND, 0)
        sizer_1.Add(self.label_5, 0, 0, 0)
        sizer_1.Add(self.txtCook, 0, wx.EXPAND, 0)
        sizer_5.Add(self.btnSave, 0, wx.LEFT | wx.BOTTOM, 1)
        sizer_5.Add(self.btnCancel, 0, wx.BOTTOM, 1)
        sizer_5.Add(self.btnPrev, 0, wx.BOTTOM, 1)
        sizer_5.Add(self.btnNext, 0, wx.BOTTOM, 1)
        sizer_5.Add(self.btnOpen, 0, wx.BOTTOM, 1)
        self.btnPanel.SetSizer(sizer_5)
        sizer_1.Add(self.btnPanel, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class RecipeFrame