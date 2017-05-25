import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Line3D

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def vis_magnetic_moment(M, frame_rate, subsample=1):
    """
    Creates an animation simulating a magnetic moment vector, from the reference
    frame of the RF pulse.

    Parameters
    ----------
    M: A numpy array of shape (n_timepoints, 3), giving the path of the
      magnetic moment vector.
    frame_rate: int. The attempted frames per second.
    subsample: int. A factor to subsample frames by to speed up.
    """
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')
    def init():
        ax.clear()
        ax.plot([], [], [])
        ax.set_title('3D Bloch Simulation')
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        ax.plot([-1, 1], [0, 0], [0, 0], color='black')
        ax.plot([0, 0], [-1, 1], [0, 0], color='black')
        ax.plot([0, 0], [0, 0], [-1, 1], color='black')
        ax.set_axis_off()
        return []

    def animate(i):
        a = Arrow3D([0, M[i, 0]], [0, M[i, 1]],
                    [0, M[i, 2]], mutation_scale=20,
                    lw=4, arrowstyle="-|>", color="b")
        b = Line3D(M[:i+1, 0], M[:i+1, 1], M[:i+1, 2],
                   linestyle='--', color="red")
        ax.add_artist(a)
        ax.add_artist(b)
        return [a, b]

    anim = FuncAnimation(fig, animate, np.arange(0, np.shape(M)[0], subsample),
                         interval=1000/frame_rate, init_func=init, blit=True)
    plt.show()
