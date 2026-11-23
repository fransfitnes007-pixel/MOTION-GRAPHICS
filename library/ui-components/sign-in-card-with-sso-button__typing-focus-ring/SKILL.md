---
name: sign-in-card-with-sso-button-typing-focus-ring
description: "A clean centred login card: sunburst logo, 'Sign in to Acme', email and password inputs with a Reset password link, remember-me checkbox, black Sign In, outlined Single sign-on (SSO) button, and a footer row with Sign up. Use for any app login screen."
---

# Sign-in card with SSO button

**Code name:** Typing, focus ring.

## What you see
A white page with one centred card, 354 x 590 in the original (shown at 1.2x), 1px light border and 16px corners. From the top: a black sunburst of 12 bars about 50px across, 'Sign in to Acme' in 24px semibold, 'Welcome back! Please enter your details.' in 15px grey, an 'Email address' label with a 38px input, a 'Password' label with 'Reset password' on the right and an input with an eye icon, a black checked 'Remember me' box, a full-width `#171717` Sign In button, an outlined key-icon 'Single sign-on (SSO)' button, a hairline, and 'New to Acme? Sign up' centred in the footer. In the clip a cursor clicks the email field (a 1px dark border and soft ring appear), 'user@acme.com' is typed at about 11 characters a second, then the password field is clicked and nine dots are typed. The demo adds a click on Sign In and clears the fields at 7s to loop.

## When to use it
The default login screen for a SaaS or internal tool that offers both password and company single sign-on. It carries no motion of its own beyond focus and typing, so pair it with a page transition if you want more.

## How it works
Plain form pieces: two labelled inputs, a checkbox, two buttons and a footer. The only animated parts are the focus state and the caret. Focus swaps the input border from `#e1e1e4` to `#111` and adds a `0 0 0 3px rgba(0,0,0,.08)` ring. The demo prints typed characters with `slice(0, n)` where `n = floor((t - tStart) / charTime) + 1`, and blinks the caret on `floor(t * 2) % 2`.

```js
const n = Math.floor((t - tType) / .09) + 1      // characters typed so far
field.style.borderColor = focused ? '#111' : '#e1e1e4'
field.style.boxShadow = focused ? '0 0 0 3px rgba(0,0,0,.08)' : '0 1px 2px rgba(0,0,0,.06)'
```

## Numbers that matter
| | |
|---|---|
| Card | 354 x 590, border `#e4e4e7`, radius 16 |
| Title / sub | 24px 600 / 15px `#6b6b72` |
| Inputs | 300 x 38, radius 7, border `#e1e1e4` |
| Sign In | 302 x 38, `#171717`, white 15px 500 |
| SSO | same size, white, 1px border, key icon |
| Typing | 0.09s per character |
| Focus ring | border `#111` plus 3px `rgba(0,0,0,.08)` |

## Sound
Silent.

## Adapt it
- `brand`, `title`, `sub`: the copy and company name.
- `emailPlaceholder` and `email`: the placeholder and the scripted typing.
- The sunburst `svg` for your logo.
- `charTime`: typing speed in the demo; in your app this is the user.

## Files
- `code/demo.html` runs on its own and loops. Everything it draws is a function of time, with `CONFIG` at the top of the script.
- `media/poster.jpg` is one frame.

## Credit
Idea: "Login With SSO" by ephraimduncan on 21st.dev (https://21st.dev/@ephraimduncan/components/login-08), MIT. This demo is an original recreation written from the public preview.
