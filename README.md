# Yasuo

This small lib is produced some functions to support convert string

## Setup

```commandline
pip install yasuo
```

## Convert a string to Vietnamese without accents

```python
yasuo.remove_accents('Phong Tuyệt Kỹ')  # Phong Tuyet Ky
```

## Generate Url Key

```python
yasuo.generate_url_key('Phong Tuyệt Kỹ')  # phong-tuyet-ky
```