import numpy as np

#Shape is a 2*n array, s[0] is x value
#s[1] is y value.

class Shape:

    def __init__(self, xs=None, ys=None, arr=None):
        '''
        __init__(self, xs=None, ys=None, arr=None)
            __init__ of class Shape.

        args:
            xs, ys: 1-D array like with same size
                xs and ys value of the Shape.

            arr: 2-D array with shape (2, n)
                arr[0] will be xs, arr[1] will be ys.
                will overwrite xs, ys arg.
        '''
        if arr is not None:
            self.arr = arr.copy()
        elif xs is not None and ys is not None:
            self.arr = np.array([xs, ys])
        else:
            self.arr = np.array([[], []])

    def get_array(self):
        '''
        get_array(self)
            Return a array of the Shape.

        returns:
            np.ndarray with shape (2, n), where n is points
            number.
        '''
        return self.arr

    def set_array(self, arr):
        '''
        set_array(self, arr)
            Set array of this Shape

        args:
            arr: 2-D array like with shape (2, n)
        '''
        self.arr = arr.copy()

    def rotate(self, theta, unit='deg', update=False):
        '''
        rotate(self, theta, unit='deg', update=False)
            Rotate Shape clockwise with theta

        args:
            shape: Shape
                A Shape object to be rotated.
    
            theta: float
                Angle to rotate clockwise.

            unit: str
                Choose from ['deg', 'rad'], unit of theta.

            update: bool
                If update is True, self will be changed.
                Default is False.
    
        returns:
            A rotated Shape object
        '''
        if unit == 'rad':
            pass
        elif unit == 'deg':
            theta = theta/180.*np.pi
        
        r_mat = np.array([[np.cos(theta), np.sin(theta)],
                          [-np.sin(theta), np.cos(theta)]])

        if update:
            self.set_array(r_mat.dot(self.get_array()))
            return self
        else:
            return Shape(arr=r_mat.dot(self.get_array()))

    def scale(self, x=1, y=1, update=False):
        '''
        scale(self, x=1, y=1)
            Rescale the Shape, all point of the Shape will be 
            multiplied by x and y.

        args:
            x, y: float
                scale of xs and ys.

            update: bool
                Whether to change the Shape itself.
                Default is False.

        returns:
            A rescaled Shape object.
        '''
        if update:
            self.arr[0] = self.arr[0] * x
            self.arr[1] = self.arr[1] * y
            return self
        else:
            tarr = self.get_array().copy()
            tarr[0] = tarr[0] * x
            tarr[1] = tarr[1] * y
            return Shape(arr=tarr)

    def move(self, x=0., y=0., update=False):
        '''
        move(self, x=0, y=0, update=False)
            Move the Shape with `x` right, `y` up.
            Call after `scale` and `rotate`.

        args:
            x, y: float
                right and up to move.

            update: bool
                Whether the Shape will be changed.

        returns:
            A moved Shape object.
        '''
        if update:
            self.arr[0] = self.arr[0] + x
            self.arr[1] = self.arr[1] + y
            return self
        else:
            tarr = self.get_array().copy()
            tarr[0] = tarr[0] + x
            tarr[1] = tarr[1] + y
            return Shape(arr=tarr)

    def add_array(self, arr, update=False):
        '''
        add_array(self, arr, update=False):
            Add a group of points to this Shape.

        args:
            arr: 2-D array like.

            update: bool
                Whether to change the Shape itself.

        returns:
            A Shape object with more points.
        '''
        if update:
            self.set_array(np.concatenate((self.get_array(), arr), axis=1))
            return self
        else:
            return Shape(arr=np.concatenate((self.get_array(), arr), axis=1))

    def add_line(self, fnx, fny, ts, argx={}, argy={}, update):
        '''
        add_line(self, fnx, fny, ts, *args, **kwargs):
            Add a line defined by fnx and fny, with value of ts.

        args:
            fnx, fny: Function with 1-D array input, 1-D array output.
                Calculate xs and ys with ts.

            argx, argy: dict
                Arguments to be passed to fnx and fny.
        '''

