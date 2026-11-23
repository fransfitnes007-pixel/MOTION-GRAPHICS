---
name: accordion-listing-row-copy-fields-caret-rotate-copy-flash
description: "A list of white rows; one opens to a panel of labelled fields, each with a Copy button that flashes solid green, plus platform toggle pills and a toast. Reach for it when you need rows that hide a set of copyable fields."
---

# Accordion listing row with copy fields

**Code name:** Caret rotate and copy flash.

## What you see
Four rows with a number badge, a title, a small condition label, a monospace price and a caret. At .6s row 2 opens over .7s: the caret turns 90 degrees and a tinted panel unfolds with fields that fade up one after another: Title (with a 48/80 length counter), Category in mono, a multi-line Description, a wrap of green keyword chips, and a dashed-rule footer of platform pills. At 2.2s the Title Copy button turns solid green and reads "Copied" for 1.2s while a dark toast rises at the bottom. The same happens for Description at 3.4s and Keywords at 4.4s. From 5.3s the four platform pills switch on one by one (solid green), and at 6.2s the row turns "done": its number badge fills green and the whole row dims to 62%.

## When to use it
Content-prep tools where someone copies pieces of structured text into other sites: listings, social posts, product feeds, email variants. Any row that has one headline and several fields behind it. Not suited to rows with only two or three fields, where an inline edit is quicker.

## How it works
Each row is a button header plus a hidden body. State lives in classes: `.open` rotates the caret, `.done` dims the row and fills the badge, `.copy.ok` and `.plat[aria-pressed="true"]` fill with the accent. The copy flash is a class on the button for a moment, plus the toast.

```css
.item.open .caret{transform:rotate(90deg)}          /* caret is a right-pointing triangle, .2s transition */
.item.done{opacity:.62}
.item.done .num{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.copy.ok{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.plat[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.toast{position:fixed;left:50%;transform:translateX(-50%) translateY(20px);opacity:0;transition:opacity .18s,transform .18s}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
```

Labels are 10.5px uppercase with a mono length counter next to them, and the Copy button is pushed right with `margin-left:auto`. Values sit in white boxes on the tinted body so they read as inputs. The source toggles the body with the `hidden` attribute, with no height animation; the demo measures the body once and drives its height from t so the opening can be seen. In the demo the toast is tied to the button flash.

## Numbers that matter
| | |
|---|---|
| Row | radius 12px, 1px line border, shadow `0 1px 2px / 0 4px 14px` at 6% and 5% |
| Number badge | 26px square, radius 7px, mono 11.5px |
| Condition label | 10px uppercase, .04em; New green, Like new blue `#2C6E9B`, Good amber `#8A6100` |
| Keyword chip | accent-soft `#DCEFE6` fill, accent text, mono 11.5px, radius 6px |
| Caret / toast / pill | .2s, .18s, instant (source) |
| Demo timing | open .6 to 1.3s, copies at 2.2, 3.4, 4.4s (1.2s each), pills 5.3s on, done 6.2s, loop 7s |

## Sound
Silent.

## Adapt it
- The field list: each field is the same `.f` block (label row, value box), so add or drop freely.
- The accent colour, which drives badge, copy, keyword and pill states.
- What "done" means for your app; it can be a checkbox state instead.
- Toast text per field.

## Files
- `code/demo.html` runs on its own and loops; 7s. All data is placeholder.
