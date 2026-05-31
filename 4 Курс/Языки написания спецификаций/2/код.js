class PriceCalculator {
    constructor(baseRate = 1500, pricePerKm = 50) {
        this.baseRate = baseRate;
        this.pricePerKm = pricePerKm;
    }

    calculate(distance, vehicleType) {
        let modifier = vehicleType === 'SUV' ? 1.5 : 1.0;
        return (this.baseRate + (distance * this.pricePerKm)) * modifier;
    }
}

class Order {
    constructor(customerData) {
        this.customerName = customerData.name;
        this.phone = customerData.phone;
        this.pickupLocation = customerData.from;
        this.destination = customerData.to;
        this.status = 'New';
    }

    async save() {
        // Логика сохранения в БД или отправки в Telegram/Email
        console.log(`Заявка от ${this.customerName} сохранена.`);
    }
}