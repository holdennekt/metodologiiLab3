# stage 1
FROM golang:1.17-alpine as build

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -o build/fizzbuzz

# stage 2
FROM scratch

COPY --from=build /app/build/fizzbuzz ./build/fizzbuzz
COPY --from=build /app/templates/index.html ./templates/index.html

CMD ["./build/fizzbuzz", "serve"]
