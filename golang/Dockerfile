# stage 1: install dependencies and build
FROM golang:1.17-alpine as builder
WORKDIR /app

# install dependencies
COPY go.mod go.sum ./
RUN go mod download

# build
COPY . .
RUN go build -o build/fizzbuzz

FROM scratch
WORKDIR /
COPY --from=builder app/build/fizzbuzz .
EXPOSE 8080

CMD ["./fizzbuzz", "serve"]
