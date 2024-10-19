def using_continue():
    for i in range(5):
        if i == 2:
            continue  # Skip the rest of the loop when i is 2
        print(i)
"""
0
1
3
4
"""

def using_pass():
    for i in range(5):
        if i == 2:
            pass  # Do nothing when i is 2, but don't skip the iteration
        print(i)

"""
0
1
2
3
4
"""

"""
Your task:
Extract all the text from the <p> tags, excluding those with the class "advertisement", "related-news".
Filter out any <p> tag that contains the phrase "Read more".
Use pass to handle any empty <p> tags.
After filtering, print out the valid content.
"""

if __name__ == "__main__":
    using_continue()
    # using_pass()
































"""
    from bs4 import BeautifulSoup

    with open('continue-pass-challenge.html', 'r') as f:
        html_text = f.read()

    soup = BeautifulSoup(html_text, 'html.parser')

    for p_tag in soup.find_all('p'):
        # Check if the <p> tag has class "advertisement" or "related-news" and skip it
        if p_tag.has_attr('class') and ('advertisement' in p_tag['class'] or 'related-news' in p_tag['class']):
            continue  # Skip these <p> tags

        text = p_tag.get_text().strip()

        if not text:
            pass  # Do nothing for empty tags
        elif "Read more" in text or "Promoted" in text:
            continue  # Skip this <p> tag with filtered content
        else:
            print(text)

    print("Extraction Complete")

"""