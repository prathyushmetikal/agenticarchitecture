
import sys, os
print(">>> sys.path:", sys.path)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Tools.filereader import extract_cv_text

filename="./Docs/Resume_prathyush.docx"
text=extract_cv_text(filename)



if __name__ == "__main__":
    filename="./Docs/Resume_prathyush.docx"
    text=extract_cv_text(filename)
    print(text)


#  uv run python -m Tools.testfilter
# >>
# Sample PDF File for Testing & Practice
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce id ligula ac quam aliquet
# venenatis. Ut at ligula tincidunt, sollicitudin purus nec, blandit metus. Sed auctor
# venenatis purus, et venenatis ipsum. Nulla facilisi. Pellentesque habitant morbi tristique
# senectus et netus et malesuada fames ac turpis egestas. Proin bibendum purus nisl, at
# volutpat risus sagittis at. Sed gravida feugiat libero, et placerat libero aliquet eget. Nam
# non risus sit amet felis accumsan tristique. Nulla facilisi. Curabitur sit amet odio odio.
# Nunc nec bibendum eros, nec convallis ligula.
# Vivamus bibendum elit sed massa feugiat, in tristique eros vestibulum. Integer at erat
# volutpat, vestibulum enim eu, ultricies justo. Praesent lacinia venenatis tellus vel
# congue. Curabitur non libero id urna mattis eleifend. Nulla facilisi. Donec sed eleifend
# massa. Fusce nec ex vel odio lacinia egestas. Suspendisse sed ex ut urna tincidunt
# semper at in ex. Vestibulum et justo eget orci posuere rhoncus. Sed vel enim euismod,
# sollicitudin urna nec, fermentum massa. Nulla facilisi. Donec gravida ligula libero, id
# dapibus ligula vulputate a. Nulla facilisi.
# You can get more free sample data at https://www.slingacademy.com/cat/sample-data/
# Happy coding & have a nice day!