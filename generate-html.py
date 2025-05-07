import os

# Path to the folder where your SVG files are located
svg_folder_path = 'assets'  # Change this to the path where your SVGs are stored
output_file_path = 'index.html'

# Read all SVG files from the folder
svg_files = [f for f in os.listdir(svg_folder_path) if f.endswith('.svg')]

# Start HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SVG Gallery</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      height: 100vh;
      background-color: #f0f0f0;
    }
    .svg-container {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
      padding: 20px;
    }
    .svg-container object {
      width: 100px;
      height: 100px;
    }
  </style>
</head>
<body>

  <h1>SVG Gallery</h1>
  <div class="svg-container">
"""

# Add each SVG file to the HTML content
for svg_file in svg_files:
    html_content += f'<object type="image/svg+xml" data="{svg_folder_path}/{svg_file}">{svg_file}</object>\n'

# Close the HTML content
html_content += """
  </div>
</body>
</html>
"""

# Write the content to the index.html file
with open(output_file_path, 'w') as f:
    f.write(html_content)

print(f'index.html has been generated in the current directory!')
