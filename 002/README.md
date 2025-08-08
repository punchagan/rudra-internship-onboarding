# "Hello, Python venv"

Goal: learn to create and use an isolated Python virtual environment

## Tasks

1. Locate/confirm Python ≥ 3.11 on your MacBook. If you only have an older
   system Python, research how to install a newer one and document what you
   did.

2. Inside this repo, use this task directory (`002`) to do the following work.

3. Create a virtual environment using `python -m venv` (older tools like
   virtualenv etc might show up on your web searches, but prefer using the
   built-in venv module).

4. Name the env folder simply `.venv`

5. Activate the environment and ensure all subsequent Python/pip actions refer
   to that interpreter.

6. Install `numpy` into the `venv`. **It should not be installed globally!**

7. Write `002/env_check.py` that prints the following

   ```
   Python: <version>
   pip   : <version>
   numpy : <version>
   ```

8. Deactivate the environment and ensure that the script env_check.py doesn't
   run with the global Python.
