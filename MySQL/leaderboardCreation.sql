CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;
DROP TABLE IF EXISTS `mydb`.`pongLeaderboard` ;
CREATE TABLE IF NOT EXISTS `mydb`.`pongLeaderboard` (
  `idNumber` INT NOT NULL,
  `userName` VARCHAR(45) NOT NULL,
  `numberOfWins` int NULL,
  UNIQUE INDEX `idNumber_UNIQUE` (`idNumber` ASC) VISIBLE,
  PRIMARY KEY (`idNumber`))
ENGINE = InnoDB;

