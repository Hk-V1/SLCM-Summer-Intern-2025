import os
import requests

data = {
    "commodities": {
        "wheat": {
            "correct": [
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/bf6b2639-46c2-41b6-834a-fcc8d663abcacropped8548193318420222195.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/a8854536-f23b-48ce-a6ba-1e2b193c77fccropped7489107252518614562.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/c89a573f-350a-4267-87b7-f697782d1650cropped2695513650914942219.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/46e93663-269f-410e-9331-653c91b514e8cropped4949993096271590869.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/9769df60-2c9e-4f9a-bab7-cb0242200197cropped3466763948382059349.jpg"
            ],
            "incorrect": [
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/c544da0c-9202-47a9-ba40-8e6f30efdd3bcropped1436988106243871464.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/e05e094d-6adb-4ced-bbf6-313d5aa2c62bcropped2867209456786561021.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/417a274f-60de-4530-846d-a1f7f536f7a9cropped1197697974862009648.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/5e8f36c2-2baa-4214-9c1a-7548b29d93d22025-06-16-13-36-37-528.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/03b9afe5-8741-46a1-9bf1-469867b712f22025-06-16-16-09-38-597.jpg"
            ],
            "waveoff": [
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/8be3cdea-e569-482a-8e1d-099553c7bf7bcropped1617218601056825236.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/dc1e7a2d-4bb6-4baf-9151-0ef94c5cb1f12025-06-16-15-27-48-484.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/bfd1a6ca-ea99-4032-862d-fc98f4d2aa672025-06-16-15-29-15-745.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/be5bace7-ad3e-4930-81d6-f1ed2c1aaec72025-06-16-16-49-35-494.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/bf2d1bc8-ddc0-44a2-901c-1da82a26579a2025-06-16-18-02-42-088.jpg"
            ]
        },
        "maize": {
            "correct": [
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/2fe47e8c-d7ad-4f1f-8e45-d2ed8438be43cropped1551435656072396081.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/99c3ff0d-9a64-4ac5-935f-1d8b60f7428bcropped34270174912494521.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/87d74021-7409-455c-a446-9073d6061a60cropped7947968017425865343.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/3e444fdc-6e80-412a-992e-0a9709827ccecropped7693792802593450739.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/fb1a7f81-4e89-4ab7-8947-8f23c0845a64cropped1337110569505198036.jpg"
            ],
            "incorrect": [
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/d59695ad-4212-4a81-8dd5-2ed34aab83e2cropped7705189878258858719.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/f99d79ab-0d9e-44ca-b7f3-965d944b9898cropped2095232797875599106.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/141ae929-0aac-4a94-a089-8c331cd4cd63cropped2259787278808791533.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/2ed68338-4844-437f-81c5-293e378319f1cropped1864232048098584725.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/bc1a8f2f-ea50-452f-b761-80bcd4e16e6ecropped4955552893490678504.jpg"
            ],
            "waveoff": [
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/6e70e97e-0587-40d2-adfa-a5db298469a4cropped5840038253069765189.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/278ce63e-ee73-4e78-957c-15b901bc3c0a2025-06-16-09-00-53-903.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/7d29e2a4-fd9e-4f9d-b0ca-27ac31b15e1d2025-06-16-09-12-11-137.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/05a4f415-5be7-445f-9263-15feadd8e0a62025-06-16-09-14-15-023.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/da69cd8d-9ae7-415c-8396-8b14607242692025-06-16-09-16-55-983.jpg"
            ]
        },
        "rice": {
            "correct": [
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/eda49b31-8d67-4076-aae4-8cd5b45893cb2025-06-16-12-29-48-919.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/7f32c3cd-d6a0-44c8-b2ed-21d906b238d1cropped448758306057744470.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/0537f0d8-8bf2-4caf-83d6-aa5eeb775dcccropped404804160333739726.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/b92149bb-082a-470a-8643-b2a573626c97cropped5654367495722171507.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/01457d18-799f-4241-9849-5d0082e2434bcropped9069120688684398455.jpg"
            ],
            "incorrect": [
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/67da3896-f11a-4ba9-870b-bb034fff6ed22025-06-16-15-44-52-774.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/9f1c9fbc-1182-4664-8d4d-2ee1071991e22025-06-16-17-25-25-421.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/28c13d65-fe49-49bb-8fbb-f3f11df83e1f2025-06-16-17-44-07-988.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/3bbf6d0d-84d9-4957-ba6c-1da52556b47f2025-06-17-11-43-38-303.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/bd399c62-8072-48d2-bedd-1e2d0e0713e02025-06-17-11-48-36-676.jpg"
            ],
            "waveoff": [
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/267c19af-3658-43e1-828c-a4a99b144bd0cropped7587138678654105299.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/e4f21dbe-ac43-43cb-aace-153e5e0ba9c3cropped8537264476025130752.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/ce3e3a79-698e-4886-9797-470c9a95fb992025-06-17-13-25-10-379.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/2fbfeadc-b876-423d-868d-0e8e32ef0ace2025-06-17-16-29-49-667.jpg",
                "https://d3b2ivxhn07375.cloudfront.net/fit-in/3264x3264/back-end-api/7d9465c6-4986-4937-84ef-eed2d31feb942025-06-18-14-15-14-253.jpg"
            ]
        }
    }
}

suffix_map = {
    "correct": "c",
    "incorrect": "i",
    "waveoff": "w"
}

def download_all_commodities(data):
    for commodity, categories in data["commodities"].items():
        for label, urls in categories.items():
            suffix = suffix_map[label]
            folder_name = f"{commodity}_{label}"
            os.makedirs(folder_name, exist_ok=True)

            for idx, url in enumerate(urls, 1):
                filename = f"{commodity}_{suffix}{idx}.jpg"
                filepath = os.path.join(folder_name, filename)

                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded: {filepath}")
                except Exception as e:
                    print(f"Failed: {url} -> {e}")

download_all_commodities(data)
