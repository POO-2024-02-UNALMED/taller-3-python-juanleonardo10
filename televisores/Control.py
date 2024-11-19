class Control:
    def _init_(self):
        self._tv = None

    def enlazar(self, tv):
        self._tv = tv
        if tv is not None:
            tv.setControl(self)

    def turnOn(self):
        if self._tv:
            self._tv.turnOn()

    def turnOff(self):
        if self._tv:
            self._tv.turnOff()

    def canalUp(self):
        if self._tv:
            self._tv.canalUp()

    def canalDown(self):
        if self._tv:
            self._tv.canalDown()

    def volumenUp(self):
        if self._tv:
            self._tv.volumenUp()

    def volumenDown(self):
        if self._tv:
            self._tv.volumenDown()

    def setCanal(self, canal):
        if self._tv:
            self._tv.setCanal(canal)

    def getTv(self):
        return self._tv

    def setTv(self, tv):
        self._tv = tv