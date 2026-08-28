const CACHE_NAME = "netcore-tech-v1";

const STATIC_ASSETS = [
    "/",
    "/static/manifest.json"
];


self.addEventListener(
    "install",
    function (event) {

        event.waitUntil(

            caches.open(CACHE_NAME)
                .then(
                    function (cache) {

                        return cache.addAll(
                            STATIC_ASSETS
                        );

                    }
                )

        );

        self.skipWaiting();
    }
);


self.addEventListener(
    "activate",
    function (event) {

        event.waitUntil(

            caches.keys()
                .then(
                    function (cacheNames) {

                        return Promise.all(

                            cacheNames.map(
                                function (cacheName) {

                                    if (
                                        cacheName !== CACHE_NAME
                                    ) {

                                        return caches.delete(
                                            cacheName
                                        );

                                    }

                                    return null;

                                }
                            )

                        );

                    }
                )

        );

        self.clients.claim();
    }
);


self.addEventListener(
    "fetch",
    function (event) {

        if (
            event.request.method !== "GET"
        ) {
            return;
        }


        event.respondWith(

            fetch(event.request)
                .then(
                    function (response) {

                        if (
                            response &&
                            response.status === 200 &&
                            response.type === "basic"
                        ) {

                            const responseClone =
                                response.clone();


                            caches.open(CACHE_NAME)
                                .then(
                                    function (cache) {

                                        cache.put(
                                            event.request,
                                            responseClone
                                        );

                                    }
                                );

                        }

                        return response;

                    }
                )
                .catch(
                    function () {

                        return caches.match(
                            event.request
                        );

                    }
                )

        );

    }
);