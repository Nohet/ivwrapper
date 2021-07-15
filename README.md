# ivwrapper 1.0
Asynchroniczny wrapper dla api ivall'a.

## Instalacja

Możesz zainstalować bibliotekę prosto z githuba

**Instalacja:** `pip install `<br>

## Przykładowe użycie
```python
import asyncio
import ivwrapper

iv = ivwrapper.Api()


async def main():
    joke = await iv.get_joke()
    print(joke)

if __name__ == "__main__":
    asyncio.run(main())
```
#Endpoint'y
```python
# endpoint'y
await get_joke()  # Losuje randomowy żart
await get_meme() # Losuje randomowy mem
 ```