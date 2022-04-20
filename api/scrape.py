from utils.utils import get_soup, get_status


class rpiLoc:
    @staticmethod
    def rpi_all(country: str):
        URL = f"https://rpilocator.com/?country={country}&cat=PI4"
        status = get_status(URL)
        response = get_soup(URL)

        # find table get th and td into rows
        tbody = response.find("tbody")
        containers = tbody.find_all("tr")

        if containers:
            api = []
            for container in containers:
                cells = container.find_all("td")
                product = cells[0].text
                url = cells[1].find('a')['href']
                update_status = cells[2].find("i")["class"][2]
                vendor = cells[3].text
                in_stock = cells[4].text
                price = "$" + cells[6].text[6:]
                cells = container.find_all("td")
                if update_status == "text-success":
                    api.append(
                        {
                            "product": product,
                            "url": url,
                            "vendor": vendor,
                            "in_stock": in_stock,
                            "price": price,
                        }

                    )
            data = {"status": status, "data": api}

            if status != 200:
                raise Exception("API response: {}".format(status))
            return data
        else:
            raise Exception("No data found")

    @staticmethod
    def rpi_model(country: str, gbs: int):
        URL = f"https://rpilocator.com/?country={country}&cat=PI4"
        status = get_status(URL)
        response = get_soup(URL)

        # find table get th and td into rows
        tbody = response.find("tbody")
        containers = tbody.find_all("tr")

        if containers:
            api = []
            for container in containers:
                cells = container.find_all("td")
                product = cells[0].text
                url = cells[1].find('a')['href']
                update_status = cells[2].find("i")["class"][2]
                vendor = cells[3].text
                in_stock = cells[4].text
                price = "$" + cells[6].text[6:]

                if update_status == "text-success":
                    if f"{gbs}GB" in product:
                        api.append(
                            {
                                "product": product,
                                "url": url,
                                "vendor": vendor,
                                "in_stock": in_stock,
                                "price": price,
                            }

                        )
            data = {"status": status, "data": api}

            if status != 200:
                raise Exception("API response: {}".format(status))
            return data


if __name__ == '__main__':
    print(rpiLoc.rpi_model("US", 4))
