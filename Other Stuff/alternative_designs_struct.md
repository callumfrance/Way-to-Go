Alternative Designs Structure
=============================
### Author: Callum France

##### Alternative 1
Instead of using Segments-Route-Description composite, have each route simply only contain descriptions - expand it out.

- Increases memory used - double-ups.
- Because always building from scratch, don't need to worry about loss of consistencies in objects.
- Makes it easier to use iterator pattern on a route.

##### Alternative 2
Implement UI using the State pattern.

- Each state represents the state of the program, and each state's method represents a type of input received from the user.
- This would add code-hiding to the base UI class.
- This would reduce the amount of control flow statements required in the UI class, but it would increase the amount of classes that would need to be written.
