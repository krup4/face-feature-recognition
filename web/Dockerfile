FROM golang:1.22-alpine3.19 AS builder

RUN apk update && apk add ca-certificates git gcc g++ libc-dev binutils

WORKDIR /opt

COPY /app/go.mod /app/go.sum ./
RUN go mod download && go mod verify

COPY ./app .

RUN go build -o bin/application .
FROM alpine:3.19 AS runner

RUN apk update && apk add ca-certificates libc6-compat openssh bash && rm -rf /var/cache/apk/*

WORKDIR /opt

COPY . . 

COPY --from=builder /opt/bin/application ./

# Run the application.
CMD ["bin/application"]
