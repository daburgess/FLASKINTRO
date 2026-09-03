# MDN Wed Development Course
- I created this new branch 'MyWebsite' so I can start creating a new website, separate from the FLASKINTRO course I had done originally. Thankfully, the main branch had basically none of that code so it is perfect to base this new branch off of. 
- I downloaded the Live View extension so that I can preview the website as I am building it on HTML. Later on, I'll probably have to transition away from this, but it'll be nice to remember HTML basics. 

## Your first website
- An **element** is used to wrap or enclose text content to define its structure and cause it to behave in a certain way. Examples are \<p>\</p>, etc. 
- An **attribute** modifies an *element*.
- Most HTML elements consist of an **opening tag** (such as \<body>), followed by the elements content, followed by a **closing tag** (like \</body>).

### Creating the content
#### Creating your first HTML document
- I am pasting the code as shown in the website and committing it so that I can see it later on as notes if it is later deleted or modified. 
- `<!doctype html>`: The doctype is a required preamble. In the mists of time, when HTML was young (around 1991/92), doctypes were meant to act as links to a set of rules that the HTML page had to follow to be considered good HTML, which could mean automatic error checking and other useful things. However, these days, they don't do much and are basically just needed to make sure your document behaves correctly. That's all you need to know for now.
- `<html></html>`: The \<html> element wraps all the content on the entire page and is sometimes known as the root element. It also includes the lang attribute, which sets the primary language of the document.

- `<head></head>`: The \<head> element acts as a container for all the stuff you want to include on the HTML page that isn't the content you are showing to your page's viewers. This includes things like keywords and a page description that you want to appear in search results, CSS to style the content, character set declarations, and more.
- `<meta charset="utf-8">`: This element sets the character set your document should use to UTF-8, which includes most characters from the vast majority of written languages. Essentially, it can now handle any textual content you might put on it. There is no reason not to set this, and it can help avoid some problems later on.
- `<meta name="viewport" content="width=device-width">`: This viewport element ensures the page renders at the width of the browser viewport, preventing mobile browsers from rendering pages wider than the viewport and then shrinking them down.
- `<title></title>`: The \<title> element sets the title of your page, which is the title that appears in the browser tab the page is loaded in. It is also used to describe the page when you bookmark/favorite it.
- `<body></body>`: The \<body> element contains all the content that you want to show to web users when they visit your page, whether that's text, images, videos, games, playable audio tracks, or whatever else. At the moment it only contains a single \<img> element, but we'll add more content later on.

#### Embedding images
`<img src="" alt="My test image" />`
- This embeds an image into our page in the position it appears. It does this via the **src** attribute, which contains the path to the image we want to embed.The **alt** attribute, you specify descriptive text for users who cannot see the image.
- Let's get your image displaying now:
1. Inside the **website** folder, create a new folder called **images** and put your image of choice in there. 
2. Inside the `<img>` tag's **src** attribute value, enter the path to your image. Since the folder containing the image is in the same directory as your `index.html` file, the path will be `images/image_name.png`.
3. Replace the **alt** attribute with some descriptive text.

#### Marking up text
##### Headings
- Use `<h1></h1>`. There are 6 levels of headings, though you should only use 3 or 4. 

##### Paragraphs
- Use `<p></p>`

##### Lists
- Unordered lists: `<ul> <li></li> </ul>`
- Ordered lists: `<ol> <li></li> <ol>`

#### Creating Links
- To add a link, we use the element <a>, where a is short for "anchor". To make text within your paragraph into a link, follow these steps:
1. Wrap the text in an <a> element : `<a> Follow this link </a>`
2. Add an **href** attribute: `<a href=""> Follow this link </a>`
    - Notice the carrot after the **href** attribute.

### Styling the content
