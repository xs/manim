from manim import *

class YawAndPitch(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add colored axes
        axes = ThreeDAxes()
        axes.x_axis.set_color(RED)
        axes.y_axis.set_color(BLUE)
        axes.z_axis.set_color(GREEN)
        self.add(axes)

        # Sphere at origin and arrow
        sphere = Sphere(radius=0.5, color=WHITE, resolution=(20, 20)).shift(ORIGIN)
        arrow = Arrow3D(start=sphere.get_center(), end=sphere.get_center() + 2*UP, color=WHITE, thickness=0.05)

        self.add(sphere, arrow)
        self.wait(0.35)

        # Demonstrate YAW in the positive direction
        yaw_arc_positive = Arc(radius=2, start_angle=PI/2, angle=PI/2, color=YELLOW)
        yaw_arc_positive = DashedVMobject(yaw_arc_positive)

        self.play(
            Rotate(arrow, angle=PI/2, axis=OUT, about_point=ORIGIN),
            Rotate(sphere, angle=PI/2, axis=OUT, about_point=ORIGIN),
            Create(yaw_arc_positive),
        )
        self.wait(0.35)

        # Fade out yaw_arc_positive
        self.play(FadeOut(yaw_arc_positive, run_time=0.35))
        self.wait(0.35)

        # Demonstrate YAW in the negative direction
        yaw_arc_negative = Arc(radius=2, start_angle=PI, angle=-5*PI/4, color=YELLOW)
        yaw_arc_negative = DashedVMobject(yaw_arc_negative)

        self.play(
            Rotate(arrow, angle=-5*PI/4, axis=OUT, about_point=ORIGIN),
            Rotate(sphere, angle=-5*PI/4, axis=OUT, about_point=ORIGIN),
            Create(yaw_arc_negative),
        )
        self.wait(0.35)

        # Fade out yaw_arc_negative
        self.play(FadeOut(yaw_arc_negative, run_time=0.35))
        self.wait(0.35)

        # Pitch rotation using the transformed RIGHT direction after the YAW
        new_right_axis = np.dot(rotation_matrix(-3 * PI/4, OUT), RIGHT)

        pitch_arc = Arc(radius=2, start_angle=0, angle=PI/3, color=YELLOW)

        # Position the pitch arc
        pitch_arc.rotate(PI/2, axis=RIGHT, about_point=ORIGIN)  # Get it into XZ plane
        pitch_arc.rotate(-PI/4, axis=OUT, about_point=ORIGIN)  # Rotate it to the yawed orientation
        pitch_arc = DashedVMobject(pitch_arc)

        self.play(
            Rotate(arrow, angle=PI/3, axis=new_right_axis, about_point=ORIGIN),
            Rotate(sphere, angle=PI/3, axis=new_right_axis, about_point=ORIGIN),
            Create(pitch_arc)
        )
        self.wait(0.35)

        self.play(FadeOut(pitch_arc, run_time=0.35))


        # Yaw rotation using the transformed UP direction after the PITCH
        new_yaw_arc = Arc(radius=2*np.cos(PI/3), start_angle=-PI/4, angle=PI/2, color=YELLOW)

        # Position the yaw arc by translating it to the end of the arrow
        new_yaw_arc.shift( OUT * 2 * np.sin(PI/3) )
        new_yaw_arc = DashedVMobject(new_yaw_arc)

        new_up_axis = np.dot(rotation_matrix(PI/3, new_right_axis), UP)

        self.play(
            Rotate(arrow, angle=PI/2, axis=OUT, about_point=ORIGIN),
            Rotate(sphere, angle=PI/2, axis=OUT, about_point=ORIGIN),
            Create(new_yaw_arc)
        )

        self.wait(0.35)

        self.play(FadeOut(sphere), FadeOut(arrow), FadeOut(axes), FadeOut(new_yaw_arc))

if __name__ == "__main__":
    from manim import *

    scene = YawAndPitch()
    scene.render()
