class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera! ", "AND123"), "Chevrolet", "Sonic");
        uberX.setPassenger(4);
        uberX.prinDataCar();

        UberVan uberVan = new UberVan("FGH345", new Account("Andres", "Herrera"));
        uberVan.setPassenger(6);
        uberVan.prinDataCar();

        /*
         * Car car2 = new Car("QWE567", new Account("Andrea HErrera", "END112"));
         * car2.passegenger = 3;
         * car2.prinDataCar();
         */

    }
}
