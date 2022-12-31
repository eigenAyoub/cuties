%%manim Gauss

class Gauss(Scene):
  def construct(self):
    ## cdf
    cdf = Axes(
            x_range=[0, 8], y_range=[0, 1], 
            x_length = 6, y_length  = 3,
            axis_config={"include_tip": False}
            ).add_coordinates().shift(UP*2)
    cdf_labels = cdf.get_axis_labels(x_label="x", y_label="cdf(x)")
    cdf_graph = cdf.get_graph(lambda x: normal.cdf(x), x_range = [0,8], color = BLUE_C)
    #cdf_group = VGroup(cdf, cdf_labels, cdf_graph)

    ## pdf
    pdf = Axes(
            x_range=[0, 8], y_range=[0, 0.5], 
            x_length = 6, y_length  = 3,
            axis_config={"include_tip": False}
        ).add_coordinates().shift(UP*2)

    pdf_labels = pdf.get_axis_labels(x_label="x", y_label="pdf(x)")
    pdf_graph =  pdf.get_graph(lambda x: normal.pdf(x),  x_range = [0,8], color = BLUE_C)
    pdf_group = VGroup(pdf, pdf_labels, pdf_graph)

    ## brace
    brace = BraceBetweenPoints(cdf.coords_to_point(0,0),cdf.coords_to_point(0,1), direction= [-1,0,0])
    t = Text("Uniform \n Samples", font_size=20).next_to(brace, LEFT)
   

    self.play(DrawBorderThenFill(pdf), Write(pdf_labels))
    self.play(Create(pdf_graph))
    self.play(pdf_group.animate.shift(DOWN*4))

    self.play(DrawBorderThenFill(cdf), Write(cdf_labels))
    self.play(Create(cdf_graph))

    self.play(Create(brace))
    self.add(t)
    
    for i in range(20):
      x1 = uniform()
      v = 4+norm.ppf(x1)

      x2 = uniform(0, normal.pdf(v))

      dot = Dot(cdf.coords_to_point(0,x1), radius=0.04, color = RED)

      dest1 = cdf.coords_to_point(v,x1)
      dest2 = cdf.coords_to_point(v,0)
      dest3 = pdf.coords_to_point(v,normal.pdf(v))
      dest4 = pdf.coords_to_point(v,0)
      dest5 = pdf.coords_to_point(v,x2)

      self.add(dot)
      self.wait(2)
      self.play(dot.animate.shift(dest1-dot.get_center()))
      self.play(dot.animate.shift(dest2-dot.get_center()))
      self.play(dot.animate.shift(dest3-dot.get_center()))
      self.play(dot.animate.shift(dest4-dot.get_center()))
      self.play(dot.animate.shift(dest5-dot.get_center()))

      self.wait(2)