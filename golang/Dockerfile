# stage 1
FROM golang:1.17-alpine as build

WORKDIR /app
COPY go.mod go.sum /app

RUN go mod download
COPY . .

RUN CGO_ENABLED=0 go build -o /app/build/fizzbuzz

# stage 2
FROM gcr.io/distroless/static-debian11

COPY --from=build /app/build/fizzbuzz /build/fizzbuzz
COPY --from=build /app/templates/index.html /templates/index.html

CMD ["/build/fizzbuzz", "serve"]
