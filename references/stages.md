# Stages: POC, MVP, PMF

Knowing which stage the user is at is what tells you when to stop coding and start
selling. Most people building with a model do not know, so they code at every stage,
and the code gets better while the number of paying strangers stays at zero. Three
stages, each with a question that moves you to the next, and each with a rule for
when the keyboard closes.

| Stage | Plain words | The question it answers | Done when | Rails steps |
|-------|-------------|-------------------------|-----------|-------------|
| **Pre-POC** | an idea, nothing built | Is there one real person with this problem, and will a stranger pay for it on paper? | a price has been shown to strangers and at least one committed on paper, on video, or with a deposit | 1 to 28 |
| **POC**, proof of concept | the smallest thing that shows the outcome is possible | Can the outcome be produced at all, for the person on slide one? | one stranger has seen it do the thing and still wants to pay | 29 to 31 |
| **MVP**, minimum viable product | the smallest thing strangers pay for and use | Do strangers pay at the real price and keep using it? | ten paying strangers, at the real price, using it in the second month | 32 to 34 |
| **PMF**, product market fit | the market keeps coming back on its own | Does the second generation, the people who arrived cold, stay? | retention holds at the green line for cold arrivals, and revenue covers serving and reaching them | 35 to 37 |
| **Scaling** | more people, more money, more markets | Does it hold when it is not the founder in the room? | the scale gate, signed | 38 to 39 |

## When to stop coding at each stage

- **Pre-POC: do not code.** The work is the person, the outcome, the price, and the
  strangers. A pay button, a landing page, a mock-up a stranger can react to: yes.
  A product: no. The line between them: a pay button is a page with the offer, the
  price, a payment link, and whatever the stranger needs to say yes (a slot picker, a
  form), and nothing that runs after the payment; a mock-up is something a stranger
  can react to that does not do the thing. Anything that does the thing is a product. If the user insists, build with "for: nobody has paid yet" on it and
  keep score.
- **POC: code until the outcome happens once, then stop.** One path, one person, the
  thing it does, ugly. The moment it works for the person on slide one, the keyboard
  closes and the next ticket is "sit with a stranger while they use it", in person
  or with their screen shared, watching and not helping. A POC with settings, roles,
  dark mode, or a second feature is an MVP nobody asked for.
- **MVP: code only what the strangers' noes ask for.** Every ticket traces to a
  stranger's reply in `STRANGERS.md` or to the money path, and each no is first
  asked whether it is a missing feature or missing teaching; value needs to be
  taught, and a walkthrough reaches every stranger while a feature serves the one
  who asked. Polish, scale, and the
  features the founder wants wait in `DECISIONS.md`. Time splits toward selling: the
  book's rule is build to 20%, sell to 99%, and at MVP most days are selling days.
- **PMF: code to keep the second generation.** Retention and churn drive the board;
  the random ticket test runs every week; the nines go up only where a paying customer
  would notice. Growth features wait for the retention goal.
- **Scaling: only on evidence.** More people and more markets after the scale gate,
  never before.

## Placing the user

Ask in climb 1 and confirm with the evidence. The honest placement is usually lower
than the user's: a product in production with no paying stranger is pre-POC with code
attached, not MVP. Say so once, with the number that places them (strangers who paid,
at the real price, by name), write the stage in `VALUE.md` next to the rails step, and
let the stage decide the day's split between building and selling. When the stage
changes, say so, and say what closes and what opens.

## In the weeds check

The weeds check (`rituals.md`) reads the stage: detail that would be right at PMF is
weeds at POC. "This is a PMF-level feature and you are at POC with zero paying
strangers" is the sentence; then help either way.
