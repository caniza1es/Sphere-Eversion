from manim import *

class CylinderEversion(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        n = 2  # cualquier natural mayor a 2

        # definendo cilindro
        def cylinder(h, phi):
            x = np.sin(phi)
            y = np.cos(phi)
            z = h
            return np.array([x, y, z])

        # funcion parametrica para eversion
        def cylinder_eversion(h, phi):
            x = np.sin((n - 1) * phi) - h * np.sin(phi)
            y = np.cos((n - 1) * phi) + h * np.cos(phi)
            z = h * np.sin(n * phi)
            return np.array([x, y, z])

        cylinder_surface = Surface(
            lambda u, v: cylinder(u, v),
            u_range=[-1, 1],  # rango para u (h)
            v_range=[0, TAU],  # circulo para v (phi)
            resolution=(24, 24),
            fill_opacity=0.8
        )

        everted_surface = Surface(
            lambda u, v: cylinder_eversion(u, v),
            u_range=[-1, 1],  
            v_range=[0, TAU],  
            resolution=(24, 24),
            fill_opacity=0.8
        )
        
        self.add(axes, cylinder_surface)
        self.wait(2)  
        self.play(Transform(cylinder_surface, everted_surface))  
        self.begin_ambient_camera_rotation(rate=0.1)  
        self.wait(10)  

if __name__ == "__main__":
    from manim import *
    config.media_width = "100%"
    config.verbosity = "ERROR"
    scene = CylinderEversion()
    scene.render()
