# Example Steering Prompt Sequence

Verbatim user messages from the original programmatic-API goal through finalization of the public and internal designs. Spelling, punctuation, and message-internal line breaks are preserved. This is historical example material, not a normative script.

## Prompt 1

~~~text
/goal develop a easy to use programmatic interface by which a user could, in python / jupyter, train a model by pointing to a dataset and then use the trained model to reconstruct a dataset (either the same one (eg the entire object whereas training might have been on a spatial split / subset of it) or a different one) and view the results. right now things are driven mostly via cli but we want a clean programmatic flow. the implementation of this should *not* slap on additional interfaces or abstractions. it should reduce rather than increase the codebase's overall complexity (this might or might not require some prerequisite simplification / refactoring). the eventual training -> inference + visualization example script should be no more than 50 lines. it could use the run1084 dataset as an exmaple, since it's included in the repo
~~~

## Prompt 2

~~~text
approved
~~~

## Prompt 3

~~~text
let's not assume the original design is well concieved. while the review is proceeding, draft a design from scratch (no precenceptions; guided by goal conditions), then compare your design to the approved one and either select the best on e or do a synthesis
~~~

## Prompt 4

~~~text
why did you design the api without even reading index.md and groking the architecture
~~~

## Prompt 5

~~~text
" reuse the existing Torch factory’s exact authoring contract (including measurement identity) and make the native
  CLI delegate to the same function, instead of forcing Torch data semantics through the narrower public TrainingConfig." consider how to expose the correct things without creating yet another interface layer (which is forbidden)
~~~

## Prompt 6

~~~text
yes
~~~

## Prompt 7

~~~text
think about whether exposing overrides in this way is too much for a user (not saying it necessarily is but think about it
~~~

## Prompt 8

~~~text
same for the user having to do a kwargg asignment of the payload
~~~

## Prompt 9

~~~text
the default profile should be ci. this might require passing in an nphotons parameter if the dataset isnt already correctly scaled
~~~

## Prompt 10

~~~text
wouldnt it be more elegant to use nphotons to rescale the data, such that it then conforms to model expectations
relatedly it wouldnt be bad to rescalescale the probe (post diffraction rescaling) such that its L2 parseval identity matches the diffraction
~~~

## Prompt 11

~~~text
(the independent probe matching would be enforcing the same convention that the ci initializatio of s1 and s2 enforces. decide for yourself whether it's preferable / cleaner or redundant
~~~

## Prompt 12

~~~text
theres nothing wrong necessarily with idempotent saling.
(after youve finished addressing what you're woriiking on rn  consider that part of this goal's deliverable is an example script that has to include not just train -> inference but also visualization)
~~~

## Prompt 13

~~~text
dont forget to allow the user to select model (ffno, cnn, etc) by name
~~~

## Prompt 14

~~~text
consider simplifying fields such as trained.bundle_path or cryptic long names such as reconstruct_npz_barycentric
~~~

## Prompt 15

~~~text
(similar clarity / least surprise principle for names such as training_groups and n_raw_frames_selected)
~~~

## Prompt 16

~~~text
" I’m checking whether this can replace existing public doors cleanly rather than sit on top of them" dont forget that
~~~

## Prompt 17

~~~text
what are DATA and RUN
~~~

## Prompt 18

~~~text
why should the user have to construct Paths
~~~

## Prompt 19

~~~text
"This leaves the normal user with one count." how about if the user wants C>1 how do they specify that
~~~

## Prompt 20

~~~text
" My recommendation is therefore: simplify the public doors completely, fix the candidate-pool default, and retain the precise scientific field names. Do you approve that choice" yes
~~~

## Prompt 21

~~~text
before drafting plan write another more concise (<100 lines) doc (self contained but in addition to  docs/superpowers/specs/2026-08-25-programmatic-training-reconstruction-design.md  not replacing it) that explains in clear terms how the api will work from the user end (inc example(s)) and gives an idea (but not necessarrily complete description) of how it's implemented
~~~

## Prompt 22

~~~text
what's runs/ffno-c4?
~~~

## Prompt 23

~~~text
how would the user know what valid fields are or get feedback upon validation failures (not saying this is absolutely necessary for surface level api but think about it
~~~

## Prompt 24

~~~text
in addition to the spec shouldnt there be an internal architecture design that reduces rather than increases the overall complexity of the system
~~~

## Prompt 25

~~~text
the design should be as light as possible on 'sealing', 'adapters', and other such abstractions and operations of questionable necessity
~~~

