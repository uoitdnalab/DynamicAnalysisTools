Builds a Docker Environment for testing web application penetration
testing tools against the
[OWASP Benchmark Project](https://github.com/OWASP/Benchmark)

To use:
-------

1. Clone this repository

2. Inside the cloned repository:
```
git clone https://github.com/OWASP/Benchmark
```

3. Build the Docker Environment
```
docker-compose build
```

4. Run the Docker Environment
```
docker-compose up -d
```

5. Use `docker attach` to get a shell for the penetration testing container
